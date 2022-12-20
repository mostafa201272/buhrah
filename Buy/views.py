from django.shortcuts import render
import folium
import geocoder


# Create your views here.
def buy_search_page(request):

    temp = """
    
            <!-- START OF ITEM -->
            <div class="col-md-6">
                <!-- ITEM -->
                <div class="room-list-item">
                    <div class="row">
                        <div class="col-lg-12">
                            <figure class="gradient-overlay-hover link-icon">
                                <a href="#"><img src="/static/frontend/images/rooms/single/single1.jpg" class="img-fluid" alt="Image"></a>
                            </figure>
                        </div>
                        <div class="col-lg-12">
                            <div class="room-info">
                                <h3 class="room-title">
                                    <a href="#">SR 890K</a>
                                </h3>
                                
                                <p>
                                    <!-- Location Icon -->
                                    <span>
                                        <svg xmlns="http://www.w3.org/2000/svg" style="width: 18px;" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-map-pin"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                    </span>

                                    <!-- Location -->
                                    <span>17011 Hidden Treasure Cir, Friendswood, TX 77546</span>
                                </p>
                                <div class="room-services">
                                    <span>Area: 150m<sup>2</sup></span>
                                    <span>Beds: 5</span>
                                    <span>Bathrooms: 2</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- END OF ITEM -->


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
    folium.Marker([30, 30], tooltip="view", popup=temp, icon=folium.Icon(color="orange")).add_to(buy_map)
    
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