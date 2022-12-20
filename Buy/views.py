from django.shortcuts import render
import folium
import geocoder


# Create your views here.
def buy_search_page(request):

    temp = """
    
            <!-- ITEM -->
                <div class="room-list-item">
                    <div class="row">
                        <div class="col-lg-12">
                            <figure class="gradient-overlay-hover link-icon">
                                <a href="#"><img src="#" class="img-fluid" alt="Image"></a>
                            </figure>
                        </div>
                        <div class="col-lg-8">
                            <div class="room-info">
                                <h3 class="room-title">
                                    <a href="#">Vila</a>
                                </h3>
                                
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellendus animi quod adipisci quia? Laudantium quibusdam, mollitia nisi quasi perspiciatis omnis...</p>
                                <div class="room-services">
                                    <span>Area: 150m<sup>2</sup></span>
                                    <span>Beds: 5</span>
                                    <span>Bathrooms: 2</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="room-price">
                                <span class="price">SR 890K</span>
                                <a href="#" class="btn btn-sm house-search-action-btn">VIEW DETAILS</a>
                                <a href="#" class="btn btn-sm house-search-action-btn">Request a tour</a>
                            </div>
                        </div>
                    </div>
                </div>


    """

    # Create Location Object
    location = geocoder.osm('الرياض')
    lat = location.lat
    lng = location.lng
    country = location.country

    # Create map instance
    buy_map = folium.Map(location=[19, -12], zoom_start=4)

    # Create Marker
    folium.Marker([lat, lng], tooltip="view", popup=temp, icon=folium.Icon(color="orange", icon='home')).add_to(buy_map)

    # Generate HTML MAP
    buy_map = buy_map._repr_html_()

    # Returned Data
    context = {
        "map": buy_map
    }

    return render(request, 'pages/frontend/Buy/buy.html', context)


def buy_house_details_page(request):
    return render(request, 'pages/frontend/Buy/buy-house-details.html')