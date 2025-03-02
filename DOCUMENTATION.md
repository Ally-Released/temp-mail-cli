# 📘 Temp Mail CLI: Technical Documentation

<div align="center">
  
![Temp Mail CLI](https://img.shields.io/badge/Temp%20Mail-CLI-8A2BE2?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.7+-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge)

</div>

## 📋 Table of Contents

- [Introduction](#introduction)
- [Architecture Overview](#architecture-overview)
- [Key Components](#key-components)
  - [TempMailClient Class](#tempmailclient-class)
  - [OTP Extraction System](#otp-extraction-system)
  - [Verification Link Detection](#verification-link-detection)
  - [User Interface](#user-interface)
- [Implementation Details](#implementation-details)
  - [Smart OTP Extraction Algorithm](#smart-otp-extraction-algorithm)
  - [Message Monitoring System](#message-monitoring-system)
  - [Rich Text Formatting](#rich-text-formatting)
  - [Interactive Menu System](#interactive-menu-system)
- [Usage Examples](#usage-examples)
- [Performance Considerations](#performance-considerations)
- [Future Enhancements](#future-enhancements)
- [Connect with the Developer](#connect-with-the-developer)

## Introduction

Temp Mail CLI is a sophisticated command-line application designed to create and manage temporary email addresses. It leverages the mail.tm API to provide users with disposable email addresses that can be used for verification purposes, account signups, or any scenario where a temporary email is needed.

What sets this application apart is its intelligent OTP (One-Time Password) extraction system, which automatically identifies and extracts verification codes from incoming emails, making the verification process seamless and efficient.

## Architecture Overview

The application follows a modular architecture with clear separation of concerns:

1. **API Client Layer**: Handles communication with the mail.tm API
2. **Business Logic Layer**: Processes emails, extracts OTPs, and manages application state
3. **User Interface Layer**: Provides both an interactive menu and a command-line interface

## Key Components

### TempMailClient Class

The `TempMailClient` class serves as the primary interface to the mail.tm API. It handles:

- Account creation with random credentials
- Authentication and token management
- Retrieving messages from the inbox
- Fetching message content