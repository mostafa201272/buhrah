from django.shortcuts import render
import folium
import geocoder


# Create your views here.
def buy_search_page(request):

    temp = """

            <a href="#" target="_blank" class="map-card-container">
   
                <div class="map-card-image">
                    <img src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/brewster-mcleod-architects-1486154143.jpg" alt="HOUSE">
                </div>
                
                <div class="map-card-details">
                    <div class="map-card-details-price">
                    <span>SR 950K</span>
                    </div>
                    <div class="map-card-details-location">
                        <p>
                            <!-- Location Icon -->
                            <span>
                                <svg xmlns="http://www.w3.org/2000/svg" style="width: 18px;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-map-pin"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                            </span>

                            <!-- Location -->
                            <span>17011 Hidden Treasure Cir, Friendswood, TX 77546</span>
                        </p>
                    </div>
                </div>
                
            </a>
    """

    # Create Location Object
    # location = geocoder.osm('الرياض')
    # lat = location.lat
    # lng = location.lng
    # country = location.country

    # Create map instance
    buy_map = folium.Map(location=[19, -12], zoom_start=4)

    # Create Marker
    # folium.Marker([lat, lng], tooltip="view", popup=temp, icon=folium.Icon(color="orange", icon='home')).add_to(buy_map)
    folium.Marker([30, 30], popup=temp, icon=folium.Icon(color="red", icon="home")).add_to(buy_map)

    # Generate HTML MAP
    buy_map.default_css.append(("buhrah_styles","/static/frontend/css/main.css",))
    buy_map = buy_map._repr_html_()
    

    # Returned Data
    context = {
        "map": buy_map
    }

    return render(request, 'pages/frontend/Buy/buy.html', context)


def buy_house_details_page(request):
    return render(request, 'pages/frontend/Buy/buy-house-details.html')