campgrounds.MapView = Backbone.View.extend({
    initialize: function () {
        this.model.on("add", this.add_marker, this);
    },

    render: function () {
        this.map = new google.maps.Map(this.el, {
            center: new google.maps.LatLng(
                this.options.latitude,
                this.options.longitude
            ),
            zoom: this.options.zoom || 10,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
    },

    add_marker: function (place) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(
                place.get('coordinates').latitude,
                place.get('coordinates').longitude),
            map: this.map,
            title: place.get('title')
        });

        var info_window = this.build_info_window(
            place, $(this.options.marker_template).html());

        google.maps.event.addListener(marker, 'click', function() {
            window.location = place.get('url');
            // info_window.open(this.map, marker);
        }.bind(this));

        return marker;
    },

    build_info_window: function (model, template) {
         return new google.maps.InfoWindow({
            content: _.template(template, model.toJSON()),
            zIndex: 100
        });
    }
});
