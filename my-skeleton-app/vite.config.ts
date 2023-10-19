import { purgeCss } from 'vite-plugin-tailwind-purgecss';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit(), purgeCss()],
	server: {
		proxy: {
			"/start-game": "http://localhost:8000",
			"/api": "http://localhost:8000",
			"/play-card": "http://localhost:8000",
			"/get-score": "http://localhost:8000",
		},
	}
});


