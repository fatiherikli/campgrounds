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
            place, $(this.options.marker_template).html(), marker);

        google.maps.event.addListener(marker, 'click', function () {
            info_window.open();
        }.bind(this));

        return marker;
    },

    build_info_window: function (model, template, marker) {
        var content = _.template(template, model.toJSON());
        return new InfoBubble({
          map: this.map,
          content: content,
          position: marker.getPosition(),
          shadowStyle: 1,
          padding: 0,
          backgroundColor: 'rgb(57,57,57)',
          borderRadius: 4,
          arrowSize: 10,
          borderWidth: 1,
          borderColor: '#2c2c2c',
          disableAutoPan: true,
          hideCloseButton: true,
          arrowPosition: 30,
          backgroundClassName: 'phoney',
          arrowStyle: 2
        });
    }
});

campgrounds.SelectPointView = campgrounds.MapView.extend({
    tagName: "div",
    id: "select-point-map",
    last_selection: null,

    initialize: function () {
        this.drawing_manager = this.build_drawing_manager()
    },

    render: function () {

        $(this.options.replace).hide().after(this.el);

        campgrounds.MapView.prototype.render.apply(this);

        this.drawing_manager.setMap(this.map);

    },

    build_drawing_manager: function () {
        var drawing_manager = new google.maps.drawing.DrawingManager({
            drawingMode: google.maps.drawing.OverlayType.MARKER,
            drawingControl: true,
            drawingControlOptions: {
                position: google.maps.ControlPosition.TOP_CENTER,
                drawingModes: [
                    google.maps.drawing.OverlayType.MARKER
                ]
            }
        });

        google.maps.event.addListener(drawing_manager,
            'markercomplete',
            this.select_marker.bind(this));

        return drawing_manager;
    },

    select_marker: function(marker) {
        if (this.last_selection) {
            // remove previous marker
            this.last_selection.setMap(null);
        }
        this.set_coordinates(marker);
        this.last_selection = marker;
    },

    set_coordinates: function (marker) {
        var position = marker.getPosition();
        $(this.options.replace).val("POINT (" + position.lng() + " " + position.lat() + ")");
    }
});
