var ChangingScenes = pc.createScript('changingScenes');

ChangingScenes.attributes.add("sceneId", {type: "string", default: "0", title: "Scene ID to Load"});

ChangingScenes.prototype.initialize = function(dt) {
    this.app.root.findByName('Button').element.on('click', function (event){
        this.changeScenes();
    }, this);
};

ChangingScenes.prototype.changeScenes = function() {
    // Get a reference to the current root object
    var oldHierarchy = this.app.root.findByName ('Root');
    
    // Load the new scene. The scene ID is found by loading the scene in the editor and 
    // taking the number from the URL
    // e.g. If the URL when Scene 1 is loaded is: https://playcanvas.com/editor/scene/475211
    // The ID is the number on the end (475211)
    this.loadScene (this.sceneId, function () {
        // Once the new scene has been loaded, destroy the old one
        oldHierarchy.destroy ();
    });
};

ChangingScenes.prototype.loadScene = function (id, callback) {
    // Get the path to the scene
    var url = id  + ".json";
    
    // Load the scenes entity hierarchy
    this.app.loadSceneHierarchy(url, function (err, parent) {
        if (!err) {
            callback(parent);
        } else {
            console.error (err);
        }
    });
};