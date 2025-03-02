import click
import requests
import json
import time
import signal
import sys
import os
import fade
import random
import webbrowser
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.markdown import Markdown
from rich import print as rprint
from rich.style import Style
from rich.theme import Theme
import pyperclip
from datetime import datetime
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.live import Live
from rich.align import Align
from rich.layout import Layout
from rich.text import Text
from rich.spinner import Spinner

# Define elegant theme with sophisticated colors
theme = Theme({
    "info": "#4682B4",  # Steel Blue
    "warning": "#708090", # Slate Gray  
    "danger": "#8B0000", # Dark Red
    "success": "#2E8B57", # Sea Green
    "primary": "#000080", # Navy
    "secondary": "#778899", # Light Slate Gray
    "accent": "#4169E1", # Royal Blue
    "highlight": "#483D8B", # Dark Slate Blue
    "special": "#9370DB", # Medium Purple
    "gold": "#DAA520", # Goldenrod (changed from FFD700)
    "platinum": "#E5E4E2", # Platinum
    "diamond": "#B9F2FF", # Diamond
    "luxury": "#8A2BE2"  # Violet
})

API_BASE_URL = "https://api.mail.tm"
console = Console(theme=theme)

# Global flag for controlling the monitoring loop
running = True

# Author and links information
AUTHOR = "ALLY"
GITHUB_LINK = "https://github.com/Ally-Released/temp-mail-cli"
GITHUB_PROFILE = "https://github.com/Ally-Released"
DISCORD_ID = "demons_arc"
DISCORD_SERVER = "https://discord.gg/tqcSc3qV3R"
YOUTUBE_CHANNEL = "https://www.youtube.com/@Ally-released"
INSTAGRAM = "https://www.instagram.com/sparkling.soul.aura/"
TWITTER = "https://x.com/Iamnotlol2"
BLUESKY = "https://bsky.app/profile/lulzsec-ally.bsky.social"

def signal_handler(sig, frame):
    """Handle Ctrl+C to gracefully exit the program"""
    global running
    console.print("\n[warning]Gracefully stopping mail monitoring...[/warning]")
    running = False

def print_gradient_text(text, gradient_type="default"):
    """Print text with gradient effects"""
    gradient_options = [
        fade.purpleblue, fade.water, fade.greenblue, fade.blackwhite, 
        fade.purplepink, fade.fire, fade.pinkred, fade.brazil, fade.random
    ]
    
    if gradient_type == "default":
        gradient_func = random.choice(gradient_options)
    elif gradient_type == "fire":
        gradient_func = fade.fire
    elif gradient_type == "water":
        gradient_func = fade.water
    elif gradient_type == "brazil":
        gradient_func = fade.brazil
    elif gradient_type == "purpleblue":
        gradient_func = fade.purpleblue
    else:
        gradient_func = fade.random
        
    gradient_text = gradient_func(text)
    print(gradient_text)

def show_preloader():
    """Display an animated preloader with elegant styling"""
    layout = Layout()
    layout.split(
        Layout(name="header"),
        Layout(name="main"),
        Layout(name="footer")
    )
    
    # Create header with elegant styling
    header_text = Text("TEMP MAIL CLI", style="bold platinum")
    header_text.stylize("luxury")
    layout["header"].update(Align.center(header_text))
    
    # Create footer with author info
    footer_text = Text(f"Created by {AUTHOR} | {GITHUB_LINK}", style="platinum")
    layout["footer"].update(Align.center(footer_text))
    
    # Create spinner animation
    spinner = Spinner("dots", text="Initializing services...", style="special")
    
    # Progress animation with more dynamic steps
    progress_steps = [
        "Establishing secure connection...",
        "Preparing mail services...",
        "Configuring interface...",
        "Optimizing performance...",
        "Finalizing setup..."
    ]
    
    # Add some visual flair with animated elements
    with Live(layout, refresh_per_second=15, screen=True):
        for step in progress_steps:
            # Create a pulsing effect
            for i in range(3):
                layout["main"].update(Align.center(Text(f"{step}", style="diamond")))
                time.sleep(0.2)
                layout["main"].update(Align.center(Text(f"{step}.", style="platinum")))
                time.sleep(0.2)
                layout["main"].update(Align.center(Text(f"{step}..", style="special")))
                time.sleep(0.2)
                layout["main"].update(Align.center(Text(f"{step}...", style="luxury")))
                time.sleep(0.2)
        
        # Show thank you message with animation
        thank_you = Text("Thanks for using Temp Mail CLI!", style="platinum")
        layout["main"].update(Align.center(thank_you))
        time.sleep(1)
        
        # Show support message with animation
        support_msg = Text("Support me on GitHub - " + GITHUB_PROFILE, style="special")
        layout["main"].update(Align.center(support_msg))
        time.sleep(1.5)
    
    # Open GitHub profile in browser
    webbrowser.open(GITHUB_PROFILE)
    
    # Show social media info
    clear_screen()
    print_logo()
    console.print(Panel(
        f"[platinum]Connect with me:[/platinum]\n" +
        f"[special]Discord:[/special] [platinum]{DISCORD_ID}[/platinum]\n" +
        f"[special]Join Discord Server:[/special] [platinum]Curious Horses[/platinum] - {DISCORD_SERVER}\n" +
        f"[special]YouTube:[/special] [platinum]Ally-released[/platinum] - {YOUTUBE_CHANNEL}\n" +
        f"[special]Instagram:[/special] [platinum]@sparkling.soul.aura[/platinum] - {INSTAGRAM}\n" +
        f"[special]Twitter:[/special] [platinum]@Iamnotlol2[/platinum] - {TWITTER}\n" +
        f"[special]BlueSky:[/special] [platinum]@lulzsec-ally.bsky.social[/platinum] - {BLUESKY}\n" +
        f"[special]GitHub:[/special] [platinum]Ally-Released[/platinum] - {GITHUB_PROFILE}",
        title="[platinum]ALLY's Social Media[/platinum]",
        border_style="luxury"
    ))
    console.print("[special]Opening YouTube channel - Subscribe for tutorials and timelapses![/special]")
    webbrowser.open(YOUTUBE_CHANNEL)
    time.sleep(1)
    webbrowser.open(DISCORD_SERVER)
    time.sleep(2)

def print_logo():
    """Print logo with gradient effect"""
    logo = """
  ▄████████  ▄█        ▄█        ▄██   ▄   
  ███    ███ ███       ███       ███   ██▄ 
  ███    ███ ███       ███       ███▄▄▄███ 
  ███    ███ ███       ███       ▀▀▀▀▀▀███ 
▀███████████ ███       ███       ▄██   ███ 
  ███    ███ ███       ███       ███   ███ 
  ███    ███ ███▌    ▄ ███▌    ▄ ███   ███ 
  ███    █▀  █████▄▄██ █████▄▄██  ▀█████▀  
             ▀         ▀                    
    """
    faded_text = fade.purpleblue(logo)
    print(faded_text)
    console.print(f"[platinum]Created by {AUTHOR}[/platinum]")

class TempMailClient:
    def __init__(self):
        self.token = None
        self.email = None
        self.password = None

    def create_account(self, domain=""):
        # Get available domains if not provided
        if not domain:
            response = requests.get(f"{API_BASE_URL}/domains")
            domains = response.json()
            if not domains.get("hydra:member"):
                console.print("[danger]No domains available[/danger]")
                return False
            domain = domains["hydra:member"][0]["domain"]

        # Generate random username
        import random
        import string
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        self.email = f"{username}@{domain}"
        self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        # Create account
        data = {"address": self.email, "password": self.password}
        response = requests.post(f"{API_BASE_URL}/accounts", json=data)
        
        if response.status_code != 201:
            console.print("[danger]Failed to create account[/danger]")
            return False

        # Get token
        auth_data = {"address": self.email, "password": self.password}
        response = requests.post(f"{API_BASE_URL}/token", json=auth_data)
        
        if response.status_code != 200:
            console.print("[danger]Failed to obtain access token[/danger]")
            return False

        self.token = response.json()["token"]
        return True

    def get_messages(self):
        if not self.token:
            console.print("[danger]Not authenticated[/danger]")
            return []

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{API_BASE_URL}/messages", headers=headers)
        
        if response.status_code != 200:
            console.print("[danger]Failed to retrieve messages[/danger]")
            return []

        return response.json()["hydra:member"]

    def get_message_content(self, message_id):
        if not self.token:
            console.print("[danger]Not authenticated[/danger]")
            return None

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(f"{API_BASE_URL}/messages/{message_id}", headers=headers)
        
        if response.status_code != 200:
            console.print("[danger]Failed to retrieve message content[/danger]")
            return None

        return response.json()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_account():
    """Load account from file"""
    try:
        with open("temp_mail_account.json", "r") as f:
            data = json.load(f)
        client = TempMailClient()
        client.email = data["email"]
        client.password = data["password"]
        client.token = data["token"]
        return client
    except FileNotFoundError:
        return None

def animate_text(text, style="special"):
    """Animate text typing effect"""
    for i in range(len(text) + 1):
        console.print(f"[{style}]{text[:i]}[/{style}]", end="\r")
        time.sleep(0.02)
    print()

def display_social_media_options():
    """Display social media connection options"""
    social_panel = Panel(
        "[platinum]Connect with ALLY:[/platinum]\n" +
        "1. [special]Join Discord Server[/special] - Curious Horses\n" +
        "2. [special]Subscribe to YouTube[/special]\n" +
        "3. [special]Follow on Instagram[/special]\n" +
        "4. [special]Follow on Twitter[/special]\n" +
        "5. [special]Follow on BlueSky[/special]\n" +
        "0. [special]Return to main menu[/special]",
        title="[platinum]Social Media[/platinum]",
        border_style="luxury"
    )
    console.print(social_panel)
    
    choice = IntPrompt.ask("\n[secondary]Select an option[/secondary]", default=0)
    
    if choice == 1:
        console.print("[special]Opening Discord server - Curious Horses[/special]")
        webbrowser.open(DISCORD_SERVER)
    elif choice == 2:
        console.print("[special]Opening YouTube channel[/special]")
        webbrowser.open(YOUTUBE_CHANNEL)
    elif choice == 3:
        console.print("[special]Opening Instagram profile[/special]")
        webbrowser.open(INSTAGRAM)
    elif choice == 4:
        console.print("[special]Opening Twitter profile[/special]")
        webbrowser.open(TWITTER)
    elif choice == 5:
        console.print("[special]Opening BlueSky profile[/special]")
        webbrowser.open(BLUESKY)

def extract_verification_links(text):
    """Extract verification links from message content"""
    # URL regex pattern
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+|http://[^\s<>"]+'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Filter for verification-like URLs
    verification_links = []
    verification_keywords = ['verify', 'confirmation', 'activate', 'confirm', 'validation']
    
    for url in urls:
        # Check if any verification keyword is in the URL
        if any(keyword in url.lower() for keyword in verification_keywords):
            verification_links.append(url)
        # Also include URLs that look like they might be verification links
        elif 'token' in url.lower() or 'auth' in url.lower():
            verification_links.append(url)
    
    return verification_links

def extract_otp_code(text):
    """Extract OTP verification codes from message content"""
    # Common OTP patterns
    # Digit codes of various lengths
    digit_patterns = [
        r'\b\d{4,10}\b',  # 4-10 digit code (covers most common OTP lengths)
        r'\b\d{3}\b',     # 3-digit code (some services use shorter codes)
    ]
    
    # Alphanumeric codes with common formats
    alphanumeric_patterns = [
        r'\b[A-Za-z0-9]{4,10}\b',  # 4-10 character alphanumeric code
    ]
    
    # Context patterns that often appear near OTP codes - these are the most reliable
    context_patterns = [
        r'verification code[^\d]*(\d+)',
        r'verification code[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'(?:code|pin|password)[^\d]*(\d+)',
        r'(?:code|pin|password)[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'otp[^\d]*(\d+)',
        r'otp[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'one-?time (?:code|password|pin)[^\d]*(\d+)',
        r'one-?time (?:code|password|pin)[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'(?:security|authentication|access|login) code[^\d]*(\d+)',
        r'(?:security|authentication|access|login) code[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'passcode[^\d]*(\d+)',
        r'passcode[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'(?:your|the) code (?:is|:)[^\d]*(\d+)',
        r'(?:your|the) (?:code|pin|otp) (?:is|:)[^A-Za-z0-9]*([A-Za-z0-9]{3,10})',
        r'(\d{4,8})[\s\r\n]*(?:is your|as your|is the|as the)[\s\r\n]*(?:verification|authentication|access)',
        r'code[\s\r\n]*:[\s\r\n]*([A-Za-z0-9]{3,10})',
    ]
    
    # First try context patterns as they're most reliable
    for pattern in context_patterns:
        matches = re.findall(pattern, text.lower())
        if matches:
            # Filter out matches that are likely not OTP codes (too long or too short)
            valid_matches = [m for m in matches if len(m) >= 3 and len(m) <= 10]
            if valid_matches:
                return valid_matches[0]
    
    # Look for digit patterns - prioritize 6-digit codes (most common OTP format)
    potential_codes = []
    for pattern in digit_patterns:
        matches = re.findall(pattern, text)
        potential_codes.extend(matches)
    
    # Filter out numbers that are likely not OTP codes
    filtered_codes = []
    for code in potential_codes:
        # Skip very long numbers (likely not OTP codes)
        if len(code) > 10:
            continue
        # Skip numbers that appear to be years
        if len(code) == 4 and code.startswith(('19', '20')):
            continue
        # Skip numbers that appear to be timestamps or dates
        if re.match(r'\d{10}', code):  # Unix timestamp
            continue
        filtered_codes.append(code)
    
    # Prioritize codes by length (6-digit codes are most common for OTP)
    six_digit_codes = [code for code in filtered_codes if len(code) == 6]
    if six_digit_codes:
        return six_digit_codes[0]
    
    # Then try 4-digit codes (second most common)
    four_digit_codes = [code for code in filtered_codes if len(code) == 4]
    if four_digit_codes:
        return four_digit_codes[0]
    
    # Then try any other filtered codes
    if filtered_codes:
        # Sort by length (descending) to prioritize longer codes which are more likely to be OTPs
        filtered_codes.sort(key=len, reverse=True)
        return filtered_codes[0]
    
    # If no digit patterns, try alphanumeric patterns
    for pattern in alphanumeric_patterns:
        matches = re.findall(pattern, text)
        if matches:
            # Filter out common words that might match the pattern
            common_words = ['verify', 'please', 'account', 'welcome', 'click', 'login', 'signin', 
                           'signup', 'reset', 'password', 'username', 'email', 'mobile', 'phone']
            filtered_matches = [m for m in matches if m.lower() not in common_words]
            
            # Further filter to remove likely non-OTP alphanumeric strings
            better_matches = []
            for match in filtered_matches:
                # Skip if it's all letters (likely a word)
                if match.isalpha():
                    continue
                # Skip if it's too long or too short
                if len(match) < 4 or len(match) > 10:
                    continue
                better_matches.append(match)
                
            if better_matches:
                return better_matches[0]
    
    return None

def display_menu():
    """Display the menu interface"""
    clear_screen()
    print_logo()
    
    # Create a panel for the menu with elegant styling
    menu_panel = Panel(
        "[luxury]Temporary Email Service[/luxury]",
        border_style="platinum",
        padding=(1, 2)
    )
    console.print(menu_panel)
    
    # Check if account exists
    client = load_account()
    if client:
        email_text = f"Your Email Address: {client.email}"
        print_gradient_text(email_text, "purpleblue")
    
    # Services header in ASCII - smaller size
    services_ascii = """
  ___  ___ _ ____   ___ ___ ___ ___ 
 / __|/ _ \ '__\ \ / / |_ _/ __/ _ \\
 \__ \  __/ |   \ V /| || | (_|  __/
 |___/\___|_|    \_/ |_||_|\___\___|
    """
    print_gradient_text(services_ascii, "fire")
    
    console.print("1. [success]Create[/success] new email")
    console.print("2. [primary]View[/primary] messages")
    console.print("3. [secondary]Read[/secondary] message")
    console.print("4. [accent]Monitor[/accent] incoming messages")
    console.print("5. [info]Copy[/info] email address")
    
    # Connect & Support header in ASCII - smaller size
    connect_ascii = """
   ___ ___  _  _ _  _ ___ ___ _____      
  / __/ _ \| \| | \| | __/ __|_   _|     
 | (_| (_) | .` | .` | _| (__  | |    
  \___\___/|_|\_|_|\_|___\___| |_|       
    """
    print_gradient_text(connect_ascii, "purpleblue")
    console.print("6. [special]Connect[/special] with ALLY")
    console.print("0. [warning]Exit[/warning] service")
    
    # Add a separator
    print_gradient_text("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", "water")
    
    return client

def menu():
    """Launch interactive interface"""
    # Show preloader on first run
    show_preloader()
    
    while True:
        client = display_menu()
        
        choice = IntPrompt.ask("\n[luxury]Please select your desired service[/luxury]", default=0)
        
        if choice == 0:
            animate_text("Thank you for using Temporary Mail Services", "platinum")
            break
            
        elif choice == 1:
            # Create new account
            clear_screen()
            creating_email_ascii = """
   ___ ___ ___   _ _____ ___ _  _  ___   ___ __  __   _   ___ _    
  / __| _ \ __| /_\_   _|_ _| \| |/ __| | __|  \/  | /_\ |_ _| |   
 | (__|   / _| / _ \| |  | || .` | (_ | | _|| |\/| |/ _ \ | || |__ 
  \___|_|_\___/_/ \_\_| |___|_|\_|\___| |___|_|  |_/_/ \_\___|____|
            """
            print_gradient_text(creating_email_ascii, "fire")
            client = TempMailClient()
            
            with Progress(
                SpinnerColumn(spinner_name="dots", style="special"),
                TextColumn("[special]{task.description}[/special]"),
                BarColumn(complete_style="#000080"),
                TimeElapsedColumn()
            ) as progress:
                task = progress.add_task("[special]Establishing credentials...[/special]", total=100)
                
                # Simulate steps in account creation
                progress.update(task, advance=20, description="Connecting to secure servers...")
                time.sleep(0.5)
                
                progress.update(task, advance=20, description="Generating secure credentials...")
                time.sleep(0.5)
                
                progress.update(task, advance=20, description="Establishing secure connection...")
                time.sleep(0.5)
                
                # Actually create the account
                success = client.create_account()
                
                progress.update(task, advance=20, description="Finalizing account setup...")
                time.sleep(0.5)
                
                progress.update(task, advance=20, description="Completing setup...")
                time.sleep(0.5)
                
                if success:
                    console.print("\n[platinum]Email Successfully Created![/platinum]\n")
                    
                    console.print(Panel.fit(
                        f"[bold platinum]EMAIL:[/bold platinum] [luxury]{client.email}[/luxury]\n\n"
                        f"[bold platinum]PASSWORD:[/bold platinum] [luxury]{client.password}[/luxury]",
                        border_style="special",
                        title="[bold]Your Credentials[/bold]"
                    ))
                    
                    pyperclip.copy(client.email)
                    console.print("\n[platinum]Email Address Copied to Clipboard[/platinum]")
                    
                    # Save credentials
                    with open("temp_mail_account.json", "w") as f:
                        json.dump({
                            "email": client.email,
                            "password": client.password,
                            "token": client.token
                        }, f)
            
            input("\n[secondary]Press Enter to return to Services...[/secondary]")
            
        elif choice == 2:
            # Check messages
            clear_screen()
            if not client:
                console.print("[danger]No active account. Please create one first.[/danger]")
                input("\n[secondary]Press Enter to return to Services...[/secondary]")
                continue
                
            print_gradient_text("Messages", "brazil")
            
            with Progress(
                SpinnerColumn(spinner_name="dots", style="special"),
                TextColumn("[special]{task.description}[/special]")
            ) as progress:
                task = progress.add_task("[special]Fetching messages...[/special]", total=100)
                progress.update(task, advance=50)
                
                messages = client.get_messages()
                progress.update(task, completed=100)
                
                # Clear the progress display before showing the table
                print("\n")
                
                if not messages:
                    console.print("[warning]No messages found in your inbox[/warning]")
                else:
                    table = Table(show_header=True, border_style="platinum")
                    table.add_column("ID", style="info")
                    table.add_column("From", style="success")
                    table.add_column("Subject", style="primary")
                    table.add_column("Received", style="secondary")
                    table.add_column("OTP/Verification", style="luxury")
                    
                    for msg in messages:
                        # Get message content to check for OTP codes and verification links
                        message_content = client.get_message_content(msg["id"])
                        otp_info = ""
                        
                        if message_content:
                            message_text = message_content.get("text", "") or message_content.get("html", "")
                            
                            # Extract OTP code if present
                            otp_code = extract_otp_code(message_text)
                            if otp_code:
                                otp_info = f"[bold gold]OTP: {otp_code}[/bold gold]"
                                
                                # Display and copy the first OTP code found
                                if not any(row[4].startswith("[bold gold]OTP:") for row in table.rows):
                                    otp_panel = Panel(
                                        f"[bold gold]{otp_code}[/bold gold]",
                                        title=f"[platinum]OTP Code from {msg['from']['address']}[/platinum]",
                                        border_style="special"
                                    )
                                    console.print(otp_panel)
                                    pyperclip.copy(otp_code)
                                    console.print(f"[platinum]OTP code [bold gold]{otp_code}[/bold gold] copied to clipboard![/platinum]")
                            
                            # Check for verification links if no OTP found
                            elif not otp_code:
                                verification_links = extract_verification_links(message_text)
                                if verification_links:
                                    otp_info = "[bold special]Verification Link[/bold special]"
                        
                        table.add_row(
                            msg["id"],
                            msg["from"]["address"],
                            msg["subject"],
                            msg["createdAt"],
                            otp_info
                        )
                    
                    console.print(table)
                    
                    # Offer to open verification links if any are found
                    verification_messages = []
                    for msg in messages:
                        message_content = client.get_message_content(msg["id"])
                        if message_content:
                            message_text = message_content.get("text", "") or message_content.get("html", "")
                            verification_links = extract_verification_links(message_text)
                            if verification_links:
                                verification_messages.append((msg, verification_links))
                    
                    if verification_messages:
                        console.print("\n[platinum]Verification links found:[/platinum]")
                        for i, (msg, links) in enumerate(verification_messages, 1):
                            console.print(f"[special]{i}.[/special] Message from [luxury]{msg['from']['address']}[/luxury] - {len(links)} link(s)")
                        
                        open_link = Prompt.ask("\n[luxury]Open a verification link? (y/n)[/luxury]", default="n")
                        if open_link.lower() == "y":
                            if len(verification_messages) == 1:
                                msg, links = verification_messages[0]
                                if len(links) == 1:
                                    console.print(f"[special]Opening verification link in browser...[/special]")
                                    webbrowser.open(links[0])
                                else:
                                    console.print(f"[platinum]Links in message from {msg['from']['address']}:[/platinum]")
                                    for i, link in enumerate(links, 1):
                                        console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                                    
                                    link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                    if 1 <= link_choice <= len(links):
                                        console.print(f"[special]Opening verification link in browser...[/special]")
                                        webbrowser.open(links[link_choice-1])
                            else:
                                msg_choice = IntPrompt.ask("[luxury]Enter the number of the message[/luxury]", default=1)
                                if 1 <= msg_choice <= len(verification_messages):
                                    msg, links = verification_messages[msg_choice-1]
                                    if len(links) == 1:
                                        console.print(f"[special]Opening verification link in browser...[/special]")
                                        webbrowser.open(links[0])
                                    else:
                                        console.print(f"[platinum]Links in message from {msg['from']['address']}:[/platinum]")
                                        for i, link in enumerate(links, 1):
                                            console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                                        
                                        link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                        if 1 <= link_choice <= len(links):
                                            console.print(f"[special]Opening verification link in browser...[/special]")
                                            webbrowser.open(links[link_choice-1])
            
            input("\n[secondary]Press Enter to return to Services...[/secondary]")
            
        elif choice == 3:
            # Read message
            clear_screen()
            if not client:
                console.print("[danger]No active account. Please create one first.[/danger]")
                input("\n[secondary]Press Enter to return to Services...[/secondary]")
                continue
                
            # First show available messages
            print_gradient_text("Messages", "purplepink")
            
            with Progress(
                SpinnerColumn(spinner_name="dots", style="special"),
                TextColumn("[special]{task.description}[/special]")
            ) as progress:
                task = progress.add_task("[special]Fetching messages...[/special]", total=100)
                progress.update(task, advance=50)
                
                messages = client.get_messages()
                progress.update(task, completed=100)
                
                # Clear the progress display before showing the table
                print("\n")
                
                if not messages:
                    console.print("[warning]No messages found in your inbox[/warning]")
                    input("\n[secondary]Press Enter to return to Services...[/secondary]")
                    continue
                else:
                    table = Table(show_header=True, border_style="platinum")
                    table.add_column("ID", style="info")
                    table.add_column("From", style="success")
                    table.add_column("Subject", style="primary")
                    
                    for msg in messages:
                        table.add_row(
                            msg["id"],
                            msg["from"]["address"],
                            msg["subject"]
                        )
                    
                    console.print(table)
            
            message_id = Prompt.ask("\n[luxury]Enter the ID of the message to read[/luxury]")
            
            with Progress(
                SpinnerColumn(spinner_name="dots", style="special"),
                TextColumn("[special]{task.description}[/special]")
            ) as progress:
                task = progress.add_task("[special]Fetching message content...[/special]", total=100)
                progress.update(task, advance=50)
                
                message = client.get_message_content(message_id)
                progress.update(task, completed=100)
                
                # Clear the progress display before showing the message
                print("\n")
                
                if message:
                    # Create a panel for the message with elegant styling
                    header = f"From: {message['from']['address']}\nSubject: {message['subject']}\nReceived: {message['createdAt']}"
                    message_panel = Panel(
                        header,
                        title="[gold]Message Details[/gold]",
                        border_style="luxury"
                    )
                    console.print(message_panel)
                    
                    content_panel = Panel(
                        message["text"] if message.get("text") else message.get("html", "No content"),
                        title="[gold]Message Content[/gold]",
                        border_style="luxury"
                    )
                    console.print(content_panel)
                    
                    # Extract OTP code if present
                    message_text = message.get("text", "") or message.get("html", "")
                    otp_code = extract_otp_code(message_text)
                    if otp_code:
                        otp_panel = Panel(
                            f"[bold gold]{otp_code}[/bold gold]",
                            title="[platinum]OTP Verification Code[/platinum]",
                            border_style="special"
                        )
                        console.print(otp_panel)
                        
                        # Automatically copy the OTP code
                        pyperclip.copy(otp_code)
                        console.print(f"[platinum]OTP code [bold gold]{otp_code}[/bold gold] copied to clipboard![/platinum]")
                    
                    # Check for verification links
                    verification_links = extract_verification_links(message_text)
                    if verification_links:
                        console.print("\n[platinum]Verification links detected:[/platinum]")
                        for i, link in enumerate(verification_links, 1):
                            console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                        
                        open_link = Prompt.ask("\n[luxury]Open a verification link? (y/n)[/luxury]", default="y")
                        if open_link.lower() == "y":
                            if len(verification_links) == 1:
                                console.print(f"[special]Opening verification link in browser...[/special]")
                                webbrowser.open(verification_links[0])
                            else:
                                link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                if 1 <= link_choice <= len(verification_links):
                                    console.print(f"[special]Opening verification link in browser...[/special]")
                                    webbrowser.open(verification_links[link_choice-1])
                else:
                    console.print("[danger]Message not found or error fetching content[/danger]")
            
            input("\n[secondary]Press Enter to return to Services...[/secondary]")
            
        elif choice == 4:
            # Monitor messages
            clear_screen()
            if not client:
                console.print("[danger]No active account. Please create one first.[/danger]")
                input("\n[secondary]Press Enter to return to Services...[/secondary]")
                continue
                
            interval = IntPrompt.ask("[luxury]Enter message check interval in seconds[/luxury]", default=30)
            
            # Set up signal handler for graceful exit
            signal.signal(signal.SIGINT, signal_handler)
            
            # Store known message IDs
            known_messages = set()
            
            # Display monitoring status with elegant styling
            print_gradient_text("Mail Monitoring", "greenblue")
            console.print(f"[platinum]Monitoring Email:[/platinum] [luxury]{client.email}[/luxury]")
            console.print(f"[platinum]Check Interval:[/platinum] [luxury]{interval} seconds[/luxury]")
            console.print("[warning]Press Ctrl+C to stop monitoring[/warning]\n")
            
            # Main monitoring loop
            global running
            running = True
            while running:
                try:
                    with Progress(
                        SpinnerColumn(spinner_name="dots", style="special"),
                        TextColumn(f"[special]Checking for new messages at {datetime.now().strftime('%H:%M:%S')}...[/special]")
                    ) as progress:
                        task = progress.add_task("", total=100)
                        progress.update(task, advance=50)
                        
                        messages = client.get_messages()
                        progress.update(task, completed=100)
                        
                        # Clear the progress display before showing new messages
                        print("\n")
                        
                        # Check for new messages
                        new_messages = []
                        for msg in messages:
                            if msg["id"] not in known_messages:
                                new_messages.append(msg)
                                known_messages.add(msg["id"])
                        
                        # Display new messages with elegant styling
                        if new_messages:
                            console.print(f"\n[platinum]{len(new_messages)} new message(s) received![/platinum]")
                            
                            table = Table(show_header=True, border_style="luxury")
                            table.add_column("ID", style="info")
                            table.add_column("From", style="success")
                            table.add_column("Subject", style="primary")
                            table.add_column("Received", style="secondary")
                            table.add_column("OTP/Verification", style="luxury")
                            
                            # Track if we've found and copied an OTP code
                            otp_found = False
                            
                            for msg in new_messages:
                                # Get message content to check for OTP codes and verification links
                                message_content = client.get_message_content(msg["id"])
                                otp_info = ""
                                
                                if message_content:
                                    message_text = message_content.get("text", "") or message_content.get("html", "")
                                    
                                    # Extract OTP code if present
                                    otp_code = extract_otp_code(message_text)
                                    if otp_code:
                                        otp_info = f"[bold gold]OTP: {otp_code}[/bold gold]"
                                    
                                    # Check for verification links if no OTP found
                                    elif not otp_code:
                                        verification_links = extract_verification_links(message_text)
                                        if verification_links:
                                            otp_info = "[bold special]Verification Link[/bold special]"
                                
                                table.add_row(
                                    msg["id"],
                                    msg["from"]["address"],
                                    msg["subject"],
                                    msg["createdAt"],
                                    otp_info
                                )
                            
                            console.print(table)
                            
                            # Process OTP codes first for all new messages
                            for msg in new_messages:
                                message_content = client.get_message_content(msg["id"])
                                if message_content:
                                    message_text = message_content.get("text", "") or message_content.get("html", "")
                                    
                                    # Extract and display OTP code if present
                                    otp_code = extract_otp_code(message_text)
                                    if otp_code:
                                        otp_panel = Panel(
                                            f"[bold gold]{otp_code}[/bold gold]",
                                            title=f"[platinum]OTP Code from {msg['from']['address']}[/platinum]",
                                            border_style="special"
                                        )
                                        console.print(otp_panel)
                                        
                                        # Automatically copy the first OTP code to clipboard
                                        if not otp_found:
                                            pyperclip.copy(otp_code)
                                            console.print(f"[platinum]OTP code [bold gold]{otp_code}[/bold gold] copied to clipboard![/platinum]")
                                            otp_found = True
                            
                            # Only process verification links if no OTP was found
                            if not otp_found:
                                for msg in new_messages:
                                    message_content = client.get_message_content(msg["id"])
                                    if message_content:
                                        message_text = message_content.get("text", "") or message_content.get("html", "")
                                        
                                        # Skip if this message has an OTP code
                                        if extract_otp_code(message_text):
                                            continue
                                        
                                        # Check for verification links
                                        verification_links = extract_verification_links(message_text)
                                        if verification_links:
                                            console.print(f"\n[platinum]Verification links detected in message from {msg['from']['address']}:[/platinum]")
                                            for i, link in enumerate(verification_links, 1):
                                                console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                                            
                                            # Automatically open the first verification link if there's only one
                                            if len(verification_links) == 1:
                                                open_link = Prompt.ask("\n[luxury]Open verification link? (y/n)[/luxury]", default="y")
                                                if open_link.lower() == "y":
                                                    console.print(f"[special]Opening verification link in browser...[/special]")
                                                    webbrowser.open(verification_links[0])
                                            else:
                                                open_link = Prompt.ask("\n[luxury]Open a verification link? (y/n)[/luxury]", default="n")
                                                if open_link.lower() == "y":
                                                    link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                                    if 1 <= link_choice <= len(verification_links):
                                                        console.print(f"[special]Opening verification link in browser...[/special]")
                                                        webbrowser.open(verification_links[link_choice-1])
                            
                            # Play notification sound (Windows only)
                            if sys.platform == 'win32':
                                import winsound
                                winsound.MessageBeep()
                    
                    # Wait for next check
                    for _ in range(interval):
                        if not running:
                            break
                        time.sleep(1)
                        
                except Exception as e:
                    console.print(f"[danger]Error: {str(e)}[/danger]")
                    time.sleep(interval)
                except KeyboardInterrupt:
                    running = False
            
            console.print("[platinum]Mail monitoring concluded[/platinum]")
            input("\n[secondary]Press Enter to return to Services...[/secondary]")
            
        elif choice == 5:
            # Copy email
            if not client:
                console.print("[danger]No active account. Please create one first.[/danger]")
            else:
                pyperclip.copy(client.email)
                console.print(f"[platinum]Email Address [luxury]{client.email}[/luxury] Copied to Clipboard[/platinum]")
            
            input("\n[secondary]Press Enter to return to Services...[/secondary]")
            
        elif choice == 6:
            # Connect with ALLY
            clear_screen()
            print_logo()
            display_social_media_options()
            input("\n[secondary]Press Enter to return to Services...[/secondary]")

@click.group()
def cli():
    """Temporary Email CLI by ALLY"""
    pass

@cli.command()
def menu_cmd():
    """Launch interactive interface"""
    menu()

@cli.command()
def create():
    """Create a new email account"""
    clear_screen()
    print_logo()
    client = TempMailClient()
    
    with Progress(
        SpinnerColumn(spinner_name="dots", style="special"),
        TextColumn("[special]{task.description}[/special]"),
        BarColumn(complete_style="#000080"),
        TimeElapsedColumn()
    ) as progress:
        task = progress.add_task("[special]Creating account...[/special]", total=100)
        
        # Simulate steps in account creation
        progress.update(task, advance=20, description="Connecting to secure servers...")
        time.sleep(0.5)
        progress.update(task, advance=20, description="Generating secure credentials...")
        time.sleep(0.5)
        
        # Actually create the account
        success = client.create_account()
        
        progress.update(task, advance=40, description="Finalizing setup...")
        time.sleep(0.5)
        progress.update(task, advance=20, description="Completing setup...")
        time.sleep(0.5)
        
        if success:
            console.print(f"[platinum]Email Successfully Created![/platinum]")
            console.print(f"[bold]Email:[/bold] [luxury]{client.email}[/luxury]")
            console.print(f"[bold]Password:[/bold] [luxury]{client.password}[/luxury]")
            pyperclip.copy(client.email)
            console.print("[platinum]Email Address Copied to Clipboard[/platinum]")
            
            # Save credentials
            with open("temp_mail_account.json", "w") as f:
                json.dump({
                    "email": client.email,
                    "password": client.password,
                    "token": client.token
                }, f)

@cli.command()
def check():
    """Check for new messages in inbox"""
    clear_screen()
    print_logo()
    try:
        with open("temp_mail_account.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        console.print("[danger]No active account. Please create one first.[/danger]")
        return

    client = TempMailClient()
    client.email = data["email"]
    client.password = data["password"]
    client.token = data["token"]

    with Progress(
        SpinnerColumn(spinner_name="dots", style="special"),
        TextColumn("[special]{task.description}[/special]")
    ) as progress:
        task = progress.add_task("[special]Checking messages...[/special]", total=100)
        progress.update(task, advance=50)
        
        messages = client.get_messages()
        progress.update(task, completed=100)
        
        # Clear the progress display before showing the table
        print("\n")
        
        if not messages:
            console.print("[warning]No messages found in your inbox[/warning]")
            return

        table = Table(show_header=True, border_style="platinum")
        table.add_column("ID", style="info")
        table.add_column("From", style="success")
        table.add_column("Subject", style="primary")
        table.add_column("Received", style="secondary")
        table.add_column("OTP/Verification", style="luxury")

        # Track if we've found and copied an OTP code
        otp_found = False

        for msg in messages:
            # Get message content to check for OTP codes and verification links
            message_content = client.get_message_content(msg["id"])
            otp_info = ""
            
            if message_content:
                message_text = message_content.get("text", "") or message_content.get("html", "")
                
                # Extract OTP code if present
                otp_code = extract_otp_code(message_text)
                if otp_code:
                    otp_info = f"[bold gold]OTP: {otp_code}[/bold gold]"
                    
                    # Display and copy the first OTP code found
                    if not otp_found:
                        otp_panel = Panel(
                            f"[bold gold]{otp_code}[/bold gold]",
                            title=f"[platinum]OTP Code from {msg['from']['address']}[/platinum]",
                            border_style="special"
                        )
                        console.print(otp_panel)
                        pyperclip.copy(otp_code)
                        console.print(f"[platinum]OTP code [bold gold]{otp_code}[/bold gold] copied to clipboard![/platinum]")
                        otp_found = True
                
                # Check for verification links if no OTP found
                elif not otp_code:
                    verification_links = extract_verification_links(message_text)
                    if verification_links:
                        otp_info = "[bold special]Verification Link[/bold special]"
            
            table.add_row(
                msg["id"],
                msg["from"]["address"],
                msg["subject"],
                msg["createdAt"],
                otp_info
            )

        console.print(table)
        
        # Only offer to open verification links if no OTP was found
        if not otp_found:
            verification_messages = []
            for msg in messages:
                message_content = client.get_message_content(msg["id"])
                if message_content:
                    message_text = message_content.get("text", "") or message_content.get("html", "")
                    verification_links = extract_verification_links(message_text)
                    if verification_links:
                        verification_messages.append((msg, verification_links))
            
            if verification_messages:
                console.print("\n[platinum]Verification links found:[/platinum]")
                for i, (msg, links) in enumerate(verification_messages, 1):
                    console.print(f"[special]{i}.[/special] Message from [luxury]{msg['from']['address']}[/luxury] - {len(links)} link(s)")
                    
                    open_link = Prompt.ask("\n[luxury]Open a verification link? (y/n)[/luxury]", default="n")
                    if open_link.lower() == "y":
                        if len(verification_messages) == 1:
                            msg, links = verification_messages[0]
                            if len(links) == 1:
                                console.print(f"[special]Opening verification link in browser...[/special]")
                                webbrowser.open(links[0])
                            else:
                                console.print(f"[platinum]Links in message from {msg['from']['address']}:[/platinum]")
                                for i, link in enumerate(links, 1):
                                    console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                                    
                                    link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                    if 1 <= link_choice <= len(links):
                                        console.print(f"[special]Opening verification link in browser...[/special]")
                                        webbrowser.open(links[link_choice-1])
                        else:
                            msg_choice = IntPrompt.ask("[luxury]Enter the number of the message[/luxury]", default=1)
                            if 1 <= msg_choice <= len(verification_messages):
                                msg, links = verification_messages[msg_choice-1]
                                if len(links) == 1:
                                    console.print(f"[special]Opening verification link in browser...[/special]")
                                    webbrowser.open(links[0])
                                else:
                                    console.print(f"[platinum]Links in message from {msg['from']['address']}:[/platinum]")
                                    for i, link in enumerate(links, 1):
                                        console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                                        
                                        link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                        if 1 <= link_choice <= len(links):
                                            console.print(f"[special]Opening verification link in browser...[/special]")
                                            webbrowser.open(links[link_choice-1])

@cli.command()
@click.argument('message_id')
def read(message_id):
    """Read a specific message by ID"""
    clear_screen()
    print_logo()
    try:
        with open("temp_mail_account.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        console.print("[danger]No active account. Please create one first.[/danger]")
        return

    client = TempMailClient()
    client.email = data["email"]
    client.password = data["password"]
    client.token = data["token"]

    with Progress(
        SpinnerColumn(spinner_name="dots", style="special"),
        TextColumn("[special]{task.description}[/special]")
    ) as progress:
        task = progress.add_task("[special]Fetching message...[/special]", total=100)
        progress.update(task, advance=50)
        
        message = client.get_message_content(message_id)
        progress.update(task, completed=100)
        
        if message:
            # Create a panel for the message with elegant styling
            header = f"From: {message['from']['address']}\nSubject: {message['subject']}\nReceived: {message['createdAt']}"
            message_panel = Panel(
                header,
                title="[gold]Message Details[/gold]",
                border_style="luxury"
            )
            console.print(message_panel)
            
            # Extract OTP code if present
            message_text = message.get("text", "") or message.get("html", "")
            otp_code = extract_otp_code(message_text)
            
            # Always check for OTP first and prioritize it
            if otp_code:
                otp_panel = Panel(
                    f"[bold gold]{otp_code}[/bold gold]",
                    title="[platinum]OTP Verification Code[/platinum]",
                    border_style="special"
                )
                console.print(otp_panel)
                
                # Automatically copy the OTP code
                pyperclip.copy(otp_code)
                console.print(f"[platinum]OTP code [bold gold]{otp_code}[/bold gold] copied to clipboard![/platinum]")
            
            # Display message content
            content_panel = Panel(
                message["text"] if message.get("text") else message.get("html", "No content"),
                title="[gold]Message Content[/gold]",
                border_style="luxury"
            )
            console.print(content_panel)
            
            # Only check for verification links if no OTP was found
            if not otp_code:
                verification_links = extract_verification_links(message_text)
                if verification_links:
                    console.print("\n[platinum]Verification links detected:[/platinum]")
                    for i, link in enumerate(verification_links, 1):
                        console.print(f"[special]{i}.[/special] [luxury]{link}[/luxury]")
                        
                        open_link = Prompt.ask("\n[luxury]Open a verification link? (y/n)[/luxury]", default="y")
                        if open_link.lower() == "y":
                            if len(verification_links) == 1:
                                console.print(f"[special]Opening verification link in browser...[/special]")
                                webbrowser.open(verification_links[0])
                            else:
                                link_choice = IntPrompt.ask("[luxury]Enter the number of the link to open[/luxury]", default=1)
                                if 1 <= link_choice <= len(verification_links):
                                    console.print(f"[special]Opening verification link in browser...[/special]")
                                    webbrowser.open(verification_links[link_choice-1])
        else:
            console.print("[danger]Message not found or error fetching content[/danger]")

@cli.command()
def status():
    """Show current email account status"""
    clear_screen()
    print_logo()
    try:
        with open("temp_mail_account.json", "r") as f:
            data = json.load(f)
        console.print(f"Current Premium Email: [luxury]{data['email']}[/luxury]")
        pyperclip.copy(data['email'])
        console.print("[gold]Premium Email Address Copied to Clipboard[/gold]")
    except FileNotFoundError:
        console.print("[danger]No active premium account. Please create one first.[/danger]")

@cli.command()
@click.option('--interval', default=30, help='Check interval in seconds (default: 30)')
def monitor(interval):
    """Continuously monitor for new messages in premium inbox (Press Ctrl+C to stop)"""
    clear_screen()
    print_logo()
    global running
    
    # Set up signal handler for graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        with open("temp_mail_account.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        console.print("[danger]No active premium account. Please create one first.[/danger]")
        console.print("[danger]No active account. Please create one first.[/danger]")
        return

    client = TempMailClient()
    client.email = data["email"]
    client.password = data["password"]
    client.token = data["token"]
    
    # Store known message IDs
    known_messages = set()
    
    # Display monitoring status
    print_gradient_text("Mail Monitoring")
    console.print(f"[success]Monitoring Email:[/success] [primary]{client.email}[/primary]")
    console.print(f"[success]Check Interval:[/success] [primary]{interval} seconds[/primary]")
    console.print("[warning]Press Ctrl+C to stop monitoring[/warning]\n")
    
    # Main monitoring loop
    running = True
    while running:
        try:
            with console.status(f"[accent]Checking for new messages at {datetime.now().strftime('%H:%M:%S')}...[/accent]"):
                messages = client.get_messages()
                
                # Check for new messages
                new_messages = []
                for msg in messages:
                    if msg["id"] not in known_messages:
                        new_messages.append(msg)
                        known_messages.add(msg["id"])
                
                # Display new messages
                if new_messages:
                    console.print(f"\n[success]{len(new_messages)} new message(s) received![/success]")
                    
                    table = Table(show_header=True, border_style="highlight")
                    table.add_column("ID", style="info")
                    table.add_column("From", style="success")
                    table.add_column("Subject", style="primary")
                    table.add_column("Received", style="secondary")
                    
                    for msg in new_messages:
                        table.add_row(
                            msg["id"],
                            msg["from"]["address"],
                            msg["subject"],
                            msg["createdAt"]
                        )
                    
                    console.print(table)
                    
                    # Play notification sound (Windows only)
                    if sys.platform == 'win32':
                        import winsound
                        winsound.MessageBeep()
            
            # Wait for next check
            for _ in range(interval):
                if not running:
                    break
                time.sleep(1)
                
        except Exception as e:
            console.print(f"[danger]Error: {str(e)}[/danger]")
            time.sleep(interval)
    
    console.print("[success]Mail monitoring concluded[/success]")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # If no arguments provided, launch interface
        menu()
    else:
        # Otherwise, use Click CLI
        cli()