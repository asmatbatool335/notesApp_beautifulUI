# NoteIt

A beautiful, professional, multi-user markdown note-taking application built with Python Flask, SQLite, and a modern HTML/CSS/JS frontend.

---

## Table of Contents
- [Overview](#overview)
- [Front-End Structure](#front-end-structure)
- [UI/UX Design](#uiux-design)
- [Current Features](#current-features)
- [Planned Features](#planned-features)
- [Setup](#setup)

---

## Overview
**NoteIt** is a desktop-style, multi-user note-taking app with a focus on beautiful, modern UI and a smooth user experience. It supports markdown notes, folders, search, and user authentication.

---

## Front-End Structure

The front-end is built using Flask's Jinja2 templating system, Bootstrap 5, and custom CSS for a modern, responsive, and visually appealing interface.

### Main Components
- **Navbar**: Always visible at the top, includes:
  - App logo (left-aligned, responsive, aspect-ratio preserved)
  - Search bar (centered, always visible, for searching notes)
  - User actions (login/logout, right-aligned)
- **Sidebar**: On the left, contains:
  - Folder navigation (list of folders, create new folder button)
- **Main Content Area**: Displays:
  - Welcome message or notes list/editor, depending on context
  - Flash messages (e.g., search results, notifications)
- **Responsive Design**: Layout adapts for desktop and mobile screens.

### Styling
- **Color Palette**: Professional blue/teal gradients, white backgrounds, and subtle shadows for a clean, modern look.
- **Logo**: Prominently displayed, size and aspect ratio controlled for best appearance.
- **Buttons & Cards**: Styled with gradients and accent colors for a lively but professional feel.

---

## UI/UX Design
- **Modern, clean, and inviting**: Uses gradients, rounded corners, and clear typography.
- **Consistent layout**: Navigation, search, and user actions are always accessible.
- **Accessibility**: Good color contrast, large clickable areas, and keyboard-friendly forms.
- **Feedback**: Flash messages for actions like search, login, and errors.

---

## Current Features
- **User Authentication**
  - Login/logout (UI in place, backend to be implemented)
- **Responsive Navbar**
  - Logo, search bar, and user actions
- **Sidebar Navigation**
  - Folder list (static for now)
- **Main Content**
  - Welcome message
  - Flash messages (e.g., search query feedback)
- **Search Bar**
  - Always visible in navbar, submits to backend
- **Professional UI**
  - Custom CSS, gradients, and modern layout

---

## Planned Features
- **User Registration**
- **Full Authentication Flow** (registration, login, logout, password hashing)
- **CRUD for Notes**
  - Create, edit, delete, and view markdown notes
  - Live markdown preview
- **CRUD for Folders**
  - Organize notes into folders
- **Search**
  - Search notes by title/content (backend integration)
- **Export**
  - Export notes as Markdown or HTML
- **User-Specific Data**
  - All notes and folders scoped to the logged-in user
- **Security**
  - CSRF protection, input validation, and secure endpoints
- **Testing**
  - Unit tests for all major features

---

## Setup
1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   flask run
   ```

---

For further development, see the code comments and modular structure in the `app/` directory. Contributions and suggestions are welcome! 