from flask import Flask, request, render_template, make_response
import io
import csv
from utility import fetch_dealer_info

# Serve root directory so /teletalk.png works
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def dealer_location():
    data = []
    column_names = []
    csv_data = ""

    if request.method == 'POST':
        short_code = request.form.get("short_code")
        hierarchy_level = request.form.get("hierarchy_level")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        if short_code and hierarchy_level and start_date and end_date:
            column_names, data = fetch_dealer_info(short_code, hierarchy_level, start_date, end_date)

        if data:
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(column_names)
            writer.writerows(data)
            csv_data = output.getvalue()

    return render_template(
        "dealer_info_portal.html",
        data=data,
        column_names=column_names,
        csv_data=csv_data
    )

@app.route('/download_dealer_info', methods=['POST'])
def download_dealer_info():
    csv_content = request.form.get("csv_content")
    filename = f"{request.form.get('short_code','dealer')}_info.csv"
    bom = '\ufeff'
    response = make_response(bom + csv_content)
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-type'] = 'text/csv; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6002)