# Dealer_info_portal
Dealer Info Portal is a Flask web app to fetch dealer data from Oracle DB using short code, hierarchy level, and date range. It shows results in a table with CSV export. Clean UI, date-only filtering, and Teletalk branding make it ideal for internal use.
Dealer Info Portal is a lightweight Flask-based web application designed to retrieve and display dealer information from an Oracle database. The tool allows users to input a dealer's short code, hierarchy level, and a date range to fetch and view detailed transactional and balance data in a user-friendly tabular format. Results can also be exported as a CSV file for offline analysis.

The backend integrates with Oracle using the oracledb module and performs optimized queries that filter records by date (ignoring timestamp), ensuring accurate and relevant output. The frontend is styled with responsive HTML and CSS for clean usability, and features like loading indicators enhance the user experience.

A Teletalk-branded logo and intuitive form inputs make this a purpose-built internal utility ideal for operational teams who need quick access to dealer-level insights.

Key features:

Date-range filtering using only the date (not time)

CSV download support

Custom Oracle SQL query integration

Minimalist and responsive design

Customizable and easy to deploy

Ideal for enterprise environments where quick access to database-driven dealer information is essential.

