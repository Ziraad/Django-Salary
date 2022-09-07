/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        '/templates/*.html',
        './templates/**/*.{html,js}',
        './node_modules/tw-elements/dist/js/**/*.js'
    ],
    theme: {
        extend: {
            fontFamily: {
                iransans: ['iransans'],
                vazir: ['vazir'],
            },
        },
    },
    plugins: [
        require('tw-elements/dist/plugin'),
    ]
}
