// src/routes/api.js

import type { RequestHandler } from '@sveltejs/kit';

export const post: RequestHandler = async (request) => {
    const response = await fetch('http://localhost:8000/start_game', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request.body), // You can pass any required data here
    });
  
    if (response.ok) {
      const data = await response.json();
      return {
        body: data,
      };
    } else {
      return {
        status: response.status,
        body: await response.text(),
      };
    }
  }
  