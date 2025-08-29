/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.jinja",
            "./templates/*.html",
            ],
  theme: {},
  plugins: [//require('@tailwindcss/forms'),
            require('@tailwindcss/typography')],
            //require("flowbite/plugin"),],
}