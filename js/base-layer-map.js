$(document).ready(function () {
	var info_form=$("#info_form");
	var wall_name=$("#wall_name");
	var wall_pic=$("#wall_pic");
	var infooverlay = new ol.Overlay({
        /*  element: container */
        stopEvent: false,
        element: info_form
    });
	var vector_layer = new ol.layer.Vector({
		name: 'my_vectorlayer',
		source: new ol.source.GeoJSON({
			projection: pixelProjection,
			url: 'js/walls.json'
		}),
		style: new ol.style.Style({
			fill: new ol.style.Fill({
				color:"#F53D71",
				opacity: 1
			}),
			stroke: new ol.style.Stroke({
				color: '#ffcc33',
				width: 2
			}),
			image: new ol.style.Circle({
				radius: 7,
				fill: new ol.style.Fill({
					color: '#ffcc33'
				})
			})
		}),
		opacity:0.5
	});
	vector_layer.on("postcompose", function () {
		var vectorlayer_features = vector_layer.getSource().getFeatures();
		vectorlayer_features.forEach(function (afeature) {

			if (afeature.get("Wall") === "A" || afeature.get("Wall") === "B"|| afeature.get("Wall") === "C"|| afeature.get("Wall") === "F") {
				afeature.setStyle(new ol.style.Style({
					fill: new ol.style.Fill({
						color: "#0AFA5E",
						opacity: 1
					}),
					stroke: new ol.style.Stroke({
						color: '#ffcc33',
						width: 2
					}),
					image: new ol.style.Circle({
						radius: 7,
						fill: new ol.style.Fill({
							color: '#ffcc33'
						})
					})
				}))
			}
		});
	})
	var pixelProjection = new ol.proj.Projection({
		code: 'pixel',
		units: 'pixels',
		extent: [0, 0, 940, 722],
		worldExtent: [0, 0, 940, 722]
	});
	var map = new ol.Map({
		controls: [
			new ol.control.Attribution(),
			new ol.control.FullScreen(),
		],
		layers: [
			new ol.layer.Image({
				source: new ol.source.ImageStatic({
					attributions: [
						new ol.Attribution({
							html: '&copy; <a href="http://xkcd.com/license.html">xkcd</a>'
						})
					],
					url: 'images/base-layer-images/base-layer-map.jpg',
					imageSize: [940, 722],
					projection: pixelProjection,
					imageExtent: pixelProjection.getExtent()
				})
			}),
			vector_layer
		],
		overlays:[infooverlay],
		target: 'map',
		view: new ol.View({
			projection: pixelProjection,
			center: ol.extent.getCenter(pixelProjection.getExtent()),
			extent: [470, 361, 470, 361],
			maxZoom: 2,
			minZoom: 2,
			zoom: 2
		})
	});
	addModifyInteraction();

	function addModifyInteraction() {
		// create select interaction
		hover_interaction = new ol.interaction.Select({
			condition: ol.events.condition.mouseMove,// make sure only the desired layer can be selected
			layers: function (vector_layer) {
				return vector_layer.get('name') === 'my_vectorlayer';
			}
		});
		click_interaction= new ol.interaction.Select({
			// make sure only the desired layer can be selected
			layers: function (vector_layer) {
				return vector_layer.get('name') === 'my_vectorlayer';
			}
		});

		map.addInteraction(hover_interaction);
		map.addInteraction(click_interaction);
		// grab the features from the select interaction to use in the modify interaction
		var selected_features = click_interaction.getFeatures();
		// when a feature is selected...
		selected_features.on('add', function (event) {
			var feature = event.element;
			console.log(feature.get("Wall"));
			if (feature.get("Wall") === "A") {
				window.location.href = "single_wall.html?wall=" + feature.get("Wall");
			}
		});
		
		var hovered_features=hover_interaction.getFeatures();
		hovered_features.on('add',function(event){
			
			var feature = event.element;
			info_form.show();
            infooverlay.setPosition([500,400]);
            //feature.getGeometry().getLastCoordinate()
            wall_name.html(feature.get("Wall"));
            wall_pic.attr("src","images/base-layer-images/"+feature.get("Wall")+".jpg"); 
            console.log("images/base-layer-images/"+feature.get("Wall")+".jpg");         
		});
		hovered_features.on('remove',function(event){
			
			
			info_form.hide();
                     
		});
	}
})
