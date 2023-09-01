# Watchlist

Watchlist is a web application that lets you create and manage your personal list of favorite movies and TV shows. Whether you want to keep track of the latest blockbusters or your all-time classics, Watchlist makes it easy to organize and review your favorite titles.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)

## Features

- **Personal Watchlists:** Create and manage multiple watchlists for movies and TV shows.
- **Detailed Reviews:** Add and edit reviews for each item in your watchlist.
- **Search and Discovery:** Browse, search, and filter movies and TV shows by title and streaming platform.
- **User Accounts:** Register and authenticate users with JWT tokens for secure access.
- **API Integration:** User-friendly API for easy integration with external applications.



**Access the Application:**

Open your web browser and go to http://localhost:8000/ to start using Watchlist.

## Usage

Here's how you can make the most of Watchlist:

- **Registration:** Sign up for a new user account.
- **Browse and Add:** Explore movies and TV shows and add them to your watchlists.
- **Review and Edit:** Share your thoughts by adding or editing reviews.
- **API Integration:** Integrate Watchlist into your applications using the user-friendly API.

## API Endpoints

Discover the powerful API behind Watchlist:

- `/list/`: Get a list of all items in your watchlist.
- `/stream/`: Explore details about streaming platforms.
- `/stream/{platform_id}/`: Get information about a specific streaming platform.
- `/list/{item_id}/`: Access details of a specific item in your watchlist.

**User Reviews**

- `/user-reviews/{username}/`: View reviews by a specific user.
- `/review-create/{item_id}/`: Create a review for an item.
- `/review/{review_id}/`: Get, update, or delete a review.

For a complete list of API endpoints and examples, refer to our API Documentation.

## Authentication

Watchlist uses token-based authentication for API access. To obtain an access token, make a POST request to `/api/token/` with your credentials.

## Installation

Get Watchlist up and running on your local machine in just a few steps:

```bash
# Clone the repository:
git clone https://github.com/yourusername/watchlist.git
cd watchlist

# Install Dependencies:
pip install -r requirements.txt

# Apply Database Migrations:
python manage.py migrate

# Start the Development Server:
python manage.py runserver
