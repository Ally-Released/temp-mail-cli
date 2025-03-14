# 🌟 Temp Mail CLI 🌟

<div align="center">
  
![Temp Mail CLI](https://img.shields.io/badge/Temp%20Mail-CLI-8A2BE2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge)

</div>

<p align="center">
  <img src="https://github.com/user-attachments/assets/18ab83b2-e3de-4a75-8a5f-f8c994e95456" alt="Temp Mail CLI Logo" width="300" />
</p>

<p align="center">
  <a href="https://github.com/Ally-Released/temp-mail-cli/releases/">
    <img src="https://img.shields.io/badge/Download-v2.0.0-blue?style=for-the-badge&logo=download" alt="Download">
  </a>
</p>

A sophisticated command-line interface for creating and managing temporary email addresses using the mail.tm API. Designed with elegance and functionality in mind, this tool provides a seamless experience for email management.

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td>
        <h3>📧 Email Management</h3>
        <ul>
          <li>Create temporary email addresses instantly</li>
          <li>Auto-copy email address to clipboard</li>
          <li>Secure credential storage</li>
        </ul>
      </td>
      <td>
        <h3>📬 Message Handling</h3>
        <ul>
          <li>Check for new messages with elegant formatting</li>
          <li>Read message contents with rich text display</li>
          <li>Continuous monitoring mode with notifications</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>
        <h3>🔍 Smart Verification</h3>
        <ul>
          <li>Intelligent OTP code extraction from messages</li>
          <li>Automatic verification link detection</li>
          <li>One-click browser opening for verification links</li>
        </ul>
      </td>
      <td>
        <h3>🎨 Beautiful Interface</h3>
        <ul>
          <li>Sophisticated color themes with gradient effects</li>
          <li>Interactive menu mode for seamless navigation</li>
          <li>ASCII art logo with dynamic gradient coloring</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <h3>🔒 Enhanced Privacy System</h3>
        <ul>
          <li>Complete request masking for total anonymity</li>
          <li>Advanced proxy integration for untraceable connections</li>
          <li>Multiple privacy-focused techniques to ensure your right to privacy</li>
          <li>Full encryption of all communications for maximum security</li>
          <li>Browser extension support for on-the-go temporary email access</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

## 🌐 Browser Extension

### Supported Browsers
<div align="center">
  <img src="https://img.shields.io/badge/Brave-orange?logo=brave&logoColor=white&style=for-the-badge" alt="Brave">
  <img src="https://img.shields.io/badge/Chrome-blue?logo=google-chrome&logoColor=white&style=for-the-badge" alt="Chrome">
  <img src="https://img.shields.io/badge/Edge-blue?logo=microsoft-edge&logoColor=white&style=for-the-badge" alt="Edge">
  <img src="https://img.shields.io/badge/Firefox-orange?logo=firefox-browser&logoColor=white&style=for-the-badge" alt="Firefox">
</div>

### Installation Options:

1. **Temporary Installation:**
    - Double-click the `install_extention.bat` file.
    - This will install the extension on your desired browser.
    - **Note:** The extension will be removed once the browser is restarted.

2. **Permanent Installation:**
    - Enable developer options in your browser's extensions settings.
    - Click on "Load Unpacked".
    - Select the folder named `browser_extention`.
    - The extension will be installed permanently.

   ![Enable Developer Options](https://github.com/user-attachments/assets/781d8bba-5969-44c5-a556-1f7ea5d75d67)
   ![Select Folder](https://github.com/user-attachments/assets/3f3faaaf-b278-46ee-9136-03d669bbe3fc)

### Lazy Mode

Our browser extension includes a powerful "Lazy Mode" feature that makes temporary email usage completely seamless:

#### Lazy Mode Features
- **Auto-fill Email Fields**: Automatically detects email input fields on websites and fills them with your temporary email.
- **Auto-submit Verification Codes**: When verification codes arrive in your inbox, they're automatically extracted and entered on the verification page.
- **Smart Context Detection**: Intelligently recognizes signup flows and verification pages.
- **Toggle Control**: Enable/disable with a single click.
- **Site-specific Settings**: Configure which websites get auto-fill and auto-verification.

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/Ally-Released/temp-mail-cli.git

# Navigate to the project directory
cd temp-mail-cli

# Install the required dependencies
pip install -r requirements.txt
```

The easiest way to use Temp Mail CLI is to double-click the `install_and_run.bat` file.

## 🚀 Usage

### Command Line Interface (CLI)

1. Open the folder containing the `install_and_run.bat` file.
2. Double-click the `install_and_run.bat` file to start the application.

Alternatively, you can run the application using the command line:

```bash
python temp_mail.py
```

### Browser Extension

To use the browser extension of Temp Mail, you first need to install it:

1. Double-click the `install_extention.bat` file to install it temporarily.
2. For permanent installation, enable developer options in your browser's extensions settings, click on "Load Unpacked", and select the `browser_extention` folder.

Once installed, click the Temp Mail extension icon to use the extension.

## 🔮 How It Works

### Smart OTP Extraction

Temp Mail CLI uses sophisticated pattern matching to automatically extract OTP codes from emails:

```python
def extract_otp_code(text):
    """Extract OTP verification codes from message content"""
    # Context patterns that often appear near OTP codes
    context_patterns = [
        r'verification code[^\d]*(\d+)',
        r'otp[^\d]*(\d+)',
        r'one-?time (?:code|password|pin)[^\d]*(\d+)',
        # More patterns...
    ]
    
    # First try context patterns as they're most reliable
    for pattern in context_patterns:
        matches = re.findall(pattern, text.lower())
        if matches:
            valid_matches = [m for m in matches if len(m) >= 3 and len(m) <= 10]
            if valid_matches:
                return valid_matches[0]
    
    # Additional fallback patterns and filtering logic...
```

The extraction algorithm prioritizes:
1. Context-based patterns (words like "verification code", "OTP", etc.)
2. Common OTP formats (6-digit codes, then 4-digit codes)
3. Intelligent filtering to avoid false positives

### Verification Link Detection

The application can also detect verification links in emails:

```python
def extract_verification_links(text):
    """Extract verification links from message content"""
    # URL regex pattern
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Filter for verification-like URLs
    verification_keywords are ['verify', 'confirmation', 'activate']
    verification_links are [url for url in urls 
                         if any(keyword in url.lower() 
                               for keyword in verification_keywords)]
    
    return verification_links
```

## 📊 Screenshots

<div align="center">
  <img src="https://github.com/user-attachments/assets/448ccb79-3487-4e6d-af11-2a9dd35593c9" alt="Main Menu" width="45%" />
  <img src="https://github.com/user-attachments/assets/f34bc0a0-31f2-40a9-87b5-8f9bba24b704" alt="Email Monitoring" width="45%" />
  <img src="https://github.com/user-attachments/assets/e642b6f8-0845-4df3-8244-783a5dfe1164" alt="Email Monitoring" width="45%" />

</div>

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Rich**: Terminal formatting and styling
- **Click**: Command-line interface creation
- **Requests**: API communication
- **PyperClip**: Clipboard integration
- **Regex**: Pattern matching for OTP extraction

## 🔗 Connect with Me

<div align="center">
  
[![BlueSky](https://img.shields.io/badge/BlueSky-lulzsec--ally.bsky.social-3B82F6?style=for-the-badge&logo=bluesky)](https://bsky.app/profile/lulzsec-ally.bsky.social)
[![X](https://img.shields.io/badge/X-Iamnotlol2-1DA1F2?style=for-the-badge&logo=twitter)](https://x.com/Iamnotlol2)
[![YouTube](https://img.shields.io/badge/YouTube-Ally--released-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/@Ally-released)

</div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [mail.tm](https://mail.tm) for providing the API

---

<div align="center">
  <p>Made with ❤️ by ALLY</p>
  <p>⭐ Star this repository if you find it useful! ⭐</p>
</div>
