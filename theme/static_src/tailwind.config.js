/** @type {import('tailwindcss').Config} */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['"DM Sans"', 'sans-serif'],
            },
            colors: {
                primary: '#1d1e20',
                secondary: '#ffffff',
                surface: '#000000',
                inverse: '#26201e',
            },
            spacing: {
                '1': '16px',
                '2': '56px',
                '3': '173px',
            },
            borderRadius: {
                'xs': '50px',
            },
        },
    },
    plugins: [],
}