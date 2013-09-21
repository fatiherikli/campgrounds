campgrounds.Place = Backbone.Model.extend({
    urlRoot: "/places"
});

campgrounds.PlaceList = Backbone.Collection.extend({
    url: "/places",
    model: campgrounds.Place
});
