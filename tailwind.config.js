/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        '/templates/*.html',
        './templates/**/*.{html,js}',
        './node_modules/tw-elements/dist/js/**/*.js'
    ],
    theme: {
        extend: {
            colors: {
                // background: '#0f172a',
                // surface: '#1E293B',
                // primary: '#9333ea',
                // primary: '#fcd535',
                // secondary: '#374151',
                danger: '#e11d48',
                // onBackground: '#9ca3af',
                // onSurface: '#d1d5db',
                // onPrimary: '#111827',
                // onSecondary: '#F9FAFB',
                // onDanger: '#ffffff'
            },
            fontFamily: {
                iransans: ['iransans'],
                vazir: ['vazir'],
            },
        },
    },
    plugins: [
        require('tw-elements/dist/plugin')
    ]
}
