# Browser Extension Implementation Guide

## Lazy Mode Technical Implementation

This document outlines the technical implementation of the "Lazy Mode" feature for the Temp Mail browser extension.

## Architecture Overview

The extension will consist of:

1. **Popup Interface**: User controls and settings
2. **Content Scripts**: For DOM manipulation and form detection
3. **Background Service Worker**: For API communication and state management
4. **Storage Module**: For saving user preferences and temporary emails

## Core Components

### 1. Email Field Detection

```javascript
// Content script
function detectEmailFields() {
  // Select all input fields that could be email fields
  const possibleEmailFields = document.querySelectorAll('input[type="email"], input[name*="email"], input[id*="email"]');
  
  possibleEmailFields.forEach(field => {
    // Add a data attribute to mark as detected
    field.dataset.tempMailDetected = true;
    
    // Add a small indicator icon to show it's detected
    addDetectionIndicator(field);
    
    // If lazy mode is enabled, auto-fill
    if (isLazyModeEnabled()) {
      autoFillEmailField(field);
    }
  });
}

// Use MutationObserver to detect dynamically added fields
const observer = new MutationObserver(mutations => {
  mutations.forEach(mutation => {
    if (mutation.addedNodes && mutation.addedNodes.length > 0) {
      // Check any new nodes for email fields
      setTimeout(detectEmailFields, 500);
    }
  });
});

// Start observing
observer.observe(document.body, {
  childList: true,
  subtree: true
});

// Run initial detection
detectEmailFields();
```

### 2. Auto-fill Implementation

```javascript
// Content script
async function autoFillEmailField(field) {
  // Get current temp email from the background service
  const email = await chrome.runtime.sendMessage({ action: "getTempEmail" });
  
  // Fill the field
  field.value = email;
  
  // Trigger input events to notify the page
  field.dispatchEvent(new Event('input', { bubbles: true }));
  field.dispatchEvent(new Event('change', { bubbles: true }));
  
  // Create a small notification
  showNotification(`Email field auto-filled with ${email}`);
}
```

### 3. OTP/Verification Code Handling

```javascript
// Background service worker
async function checkForVerificationCodes() {
  // Check temp mail inbox
  const messages = await fetchNewMessages();
  
  for (const message of messages) {
    // Extract verification codes using regex patterns
    const code = extractVerificationCode(message.content);
    
    if (code) {
      // Notify content script of all active tabs that might need the code
      const tabs = await chrome.tabs.query({active: true});
      
      for (const tab of tabs) {
        chrome.tabs.sendMessage(tab.id, {
          action: "verificationCodeReceived",
          code: code,
          messageId: message.id
        });
      }
    }
  }
}

// Set up polling
setInterval(checkForVerificationCodes, 5000);
```

### 4. Verification Form Detection & Auto-fill

```javascript
// Content script
function detectVerificationForm() {
  // Common verification input patterns
  const verificationInputs = document.querySelectorAll('input[name*="code"], input[id*="code"], input[placeholder*="code"], input[maxlength="6"], input[maxlength="4"]');
  
  verificationInputs.forEach(input => {
    input.dataset.tempMailVerificationDetected = true;
    
    // If we already have a code waiting, fill it immediately
    if (pendingVerificationCode && isLazyModeEnabled()) {
      input.value = pendingVerificationCode;
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      
      // Also try to find and click the verification button
      tryToClickVerifyButton();
      
      // Reset the pending code
      pendingVerificationCode = null;
    }
  });
}

// Listen for verification codes from background service
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "verificationCodeReceived") {
    // Store the code
    pendingVerificationCode = message.code;
    
    // Check if we already have a form to fill
    const verificationInputs = document.querySelectorAll('[data-temp-mail-verification-detected="true"]');
    
    if (verificationInputs.length > 0 && isLazyModeEnabled()) {
      // Fill the first detected input
      const input = verificationInputs[0];
      input.value = pendingVerificationCode;
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      
      // Try to find and click the verification button
      tryToClickVerifyButton();
      
      // Reset the pending code
      pendingVerificationCode = null;
    } else {
      // Show a notification with the code
      showNotification(`Verification code received: ${message.code}`);
    }
  }
});
```

### 5. Smart Button Detection

```javascript
function tryToClickVerifyButton() {
  // Try to find verification submit buttons
  const buttons = Array.from(document.querySelectorAll('button, input[type="submit"], a.btn'));
  
  // Filter buttons that are likely to be verification buttons
  const verifyButtons = buttons.filter(button => {
    const text = button.textContent.toLowerCase();
    return text.includes('verify') || 
           text.includes('confirm') || 
           text.includes('validate') ||
           text.includes('submit') ||
           text.includes('next');
  });
  
  // Click the most likely button
  if (verifyButtons.length > 0) {
    setTimeout(() => {
      verifyButtons[0].click();
    }, 1000); // Small delay to ensure the field is registered
  }
}
```

### 6. User Interface for Lazy Mode

```javascript
// popup.js
document.addEventListener('DOMContentLoaded', function() {
  // Get the lazy mode toggle
  const lazyModeToggle = document.getElementById('lazy-mode-toggle');
  
  // Initialize with saved setting
  chrome.storage.sync.get('lazyModeEnabled', function(data) {
    lazyModeToggle.checked = data.lazyModeEnabled || false;
  });
  
  // Save setting when changed
  lazyModeToggle.addEventListener('change', function() {
    chrome.storage.sync.set({
      lazyModeEnabled: lazyModeToggle.checked
    });
    
    // Notify all content scripts
    chrome.tabs.query({}, function(tabs) {
      tabs.forEach(tab => {
        chrome.tabs.sendMessage(tab.id, {
          action: "updateLazyMode",
          enabled: lazyModeToggle.checked
        });
      });
    });
  });
});
```

## Privacy Considerations

- All code processing happens on the client-side
- No data is sent to third-party servers
- User is in full control via settings
- Site blacklist/whitelist functionality for granular control
- Visual indicators for all automated actions

## Performance Optimizations

- Throttled DOM observers to reduce CPU usage
- Efficient selector patterns for quick field detection
- Cached temporary email to minimize API calls
- Batch processing of incoming messages

## Deployment Instructions

1. Package the extension for Chrome Web Store
2. Prepare Firefox Add-ons version
3. Test on popular registration flows
4. Create user documentation with examples
5. Set up a feedback mechanism for improvements

## Future Enhancements

- Machine learning to improve field detection accuracy
- Support for multi-page registration flows
- Screen recording for debugging assistance
- Add support for temporary phone numbers 