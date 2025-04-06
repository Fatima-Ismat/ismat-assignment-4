import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_info = []
        for country_data in data:
            name = country_data["name"]["common"]
            capital = country_data.get("capital", ["N/A"])[0]  # Some countries might not have a capital
            population = country_data["population"]
            area = country_data["area"]
            currencies = country_data["currencies"]
            currency = ', '.join([currencies[currency]["name"] for currency in currencies])  # Handling multiple currencies
            region = country_data["region"]

            country_info.append({
                "name": name,
                "capital": capital,
                "population": population,
                "area": area,
                "currency": currency,
                "region": region
            })
        return country_info
    else:
        return None

def main():
    st.title("Country Information App")

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info_list = fetch_country_data(country_name)

        if country_info_list:
            st.subheader("Country Information")

            for country_info in country_info_list:
                name = country_info["name"]
                capital = country_info["capital"]
                population = country_info["population"]
                area = country_info["area"]
                currency = country_info["currency"]
                region = country_info["region"]

                st.write(f"### {name}")
                st.write(f"**Capital**: {capital}")
                st.write(f"**Population**: {population}")
                st.write(f"**Area**: {area} square kilometers")
                st.write(f"**Currency**: {currency}")
                st.write(f"**Region**: {region}")
                st.write("---")
        else:
            st.error("Error: Country data not found!")

if __name__ == "__main__":
    main()


















# import streamlit
# import requests

# def fetch_country_data(country_name):
#      url = f"https://restcountries.com/v3/name/{country_name}"
#      response = requests.get(url)
#      if response.status_code == 200:
#           data = response.json()
#           country_data = data[0]
#           name = country_data["name"]
#           capital = country_data["capital"][0]
#           population = country_data["population"]
#           area = country_data["area"]
#           currency = country_data["currencies"]
#           region = country_data["region"]
#           return name,capital,population,area,currency,region
#      else:
#           return None
     
# def main():
#      st.title("Country Information App")

#      country_name = st.text_input("Enter a country name:")

#      if country_name:
#           country_info = fetch_country_data(country_name)

#           if country_info:
#                name, capital, population, area, currency, region = country_info

#                st.subheader("Country Information")
#                st.write(f"Name: {name}")
#                st.write(f"Capital: {capital}")
#                st.write(f"Population: {population}")
#                st.write(f"Area: {area} square kilometers")
#                st.write(f"Currency: {currency}")
#                st.write(f"Region: {region}")
#           else:
#                st.error("error: Country data not found!")

# if __name__ == "__main__":
#      main()

