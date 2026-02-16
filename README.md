# App Discovery Parser: AppID-Extractor

A high-performance web utility built with **Streamlit** designed to streamline the workflow for AdTech professionals, Publisher Partnership Managers, and UA specialists. This tool automates the extraction of application identifiers from raw HTML data.

## Overview
When managing large-scale publisher outreach or auditing app inventories, manually collecting Bundle IDs or App Store IDs is time-consuming. **App Discovery Parser** scans through massive amounts of HTML code (from developer pages, search results, or catalogs) and identifies unique application patterns instantly.

## Key Features
- **Multi-Store Support**: Simultaneously extracts Google Play Package Names and Apple App Store Numeric IDs.
- **Multilingual Interface**: Full support for English, Ukrainian, Russian, Spanish, French, and Portuguese.
- **Deduplication Logic**: Automatically removes duplicate entries while maintaining the original sequence found in the source code.
- **Export Ready**: Quickly copy results or download them as structured `.txt` files for use in CRM or DSP systems.
- **Modern UI**: A clean, distraction-free interface with a focus on data readability.

## Project Structure
- `app.py`: The main entry point for the Streamlit application handling UI and state.
- `parser_logic.py`: Contains the core Regex engine and localization dictionaries.
- `assets/style.css`: Custom CSS for a professional look and feel.

## Technical Details: How It Works
The tool utilizes optimized Regular Expressions (Regex) to find specific URL patterns:
- **Google Play**: Looks for `details?id=[bundle_id]` parameters.
- **App Store**: Targets `/id[numeric_id]` patterns in standard web and iTunes protocol links.

### Critical Note for Users
Many modern store pages use "Lazy Loading" (content loads only as you scroll). To ensure 100% data accuracy:
1. Open the target page in your browser.
2. Scroll to the bottom until all items are loaded.
3. Use `Ctrl+U` to view the source or `Ctrl+A` to select all content.
4. Paste the data into the parser.

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/ostinua/app-discovery-parser-appid-extractor.git](https://github.com/ostinua/app-discovery-parser-appid-extractor.git)
