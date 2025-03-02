# 🌟 Temp Mail CLI 🌟

<div align="center">
  
![Temp Mail CLI](https://img.shields.io/badge/Temp%20Mail-CLI-8A2BE2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)

![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge)

</div>

<p align="center">
  ![1__2_-removebg-preview](https://github.com/user-attachments/assets/5ccb76e9-6549-4b98-bce4-237cecfbedae)
</p>

A sophisticated command-line interface for creating and managing temporary email addresses using the mail.tm API. Designed with elegance and functionality in mind, this tool provides a seamless experience for handling disposable emails directly from your terminal.

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
  </table>
</div>

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/Ally-Released/temp-mail-cli.git

# Navigate to the project directory
cd temp-mail-cli

# Install the required dependencies
pip install -r requirements.txt

# Run the application
python temp_mail.py
```

## 🚀 Usage

### Interactive Menu Mode

The easiest way to use Temp Mail CLI is through its interactive menu:

```bash
python temp_mail.py
```

### Command Line Interface

Temp Mail CLI also provides a powerful command-line interface:

```bash
# Create a new temporary email
python temp_mail.py create

# Check for new messages
python temp_mail.py check

# Read a specific message
python temp_mail.py read MESSAGE_ID

# Monitor for new messages
python temp_mail.py monitor --interval 30
```

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
    verification_keywords = ['verify', 'confirmation', 'activate']
    verification_links = [url for url in urls 
                         if any(keyword in url.lower() 
                               for keyword in verification_keywords)]
    
    return verification_links
```

## 📊 Screenshots

<div align="center">
  <img src="https://raw.githubusercontent.com/Ally-Released/temp-mail-cli/main/assets/screenshot1.png" alt="Main Menu" width="45%" />
  <img src="https://raw.githubusercontent.com/Ally-Released/temp-mail-cli/main/assets/screenshot2.png" alt="Email Monitoring" width="45%" />
</div>

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Rich**: Terminal formatting and styling
- **Click**: Command-line interface creation
- **Requests**: API communication
- **PyperClip**: Clipboard integration
- **Regex**: Pattern matching for OTP extraction

## 🔗 Connect with the Developer

<div align="center">
  
[![GitHub](https://img.shields.io/badge/GitHub-Ally--Released-181717?style=for-the-badge&logo=github)](https://github.com/Ally-Released)
[![Discord](https://img.shields.io/badge/Discord-demons__arc-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/tqcSc3qV3R)
[![YouTube](https://img.shields.io/badge/YouTube-Ally--released-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/@Ally-released)
[![Instagram](https://img.shields.io/badge/Instagram-sparkling.soul.aura-E4405F?style=for-the-badge&logo=instagram)](https://www.instagram.com/sparkling.soul.aura/)
[![Twitter](https://img.shields.io/badge/Twitter-Iamnotlol2-1DA1F2?style=for-the-badge&logo=twitter)](https://x.com/Iamnotlol2)
[![BlueSky](https://img.shields.io/badge/BlueSky-lulzsec--ally.bsky.social-3B82F6?style=for-the-badge&logo=bluesky)](https://bsky.app/profile/lulzsec-ally.bsky.social)

</div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [mail.tm](https://mail.tm) for providing the API
- All the contributors and users of this project

---

<div align="center">
  <p>Made with ❤️ by ALLY</p>
  <p>⭐ Star this repository if you find it useful! ⭐</p>
</div>
