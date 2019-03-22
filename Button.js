var Button = pc.createScript('button');

Button.attributes.add('activeAsset', {
    type: 'asset',
    assetType: 'texture'
});


// initialize code called once per entity
Button.prototype.initialize = function() {
    
    // Get the original button texture
    this.originalTexture = this.entity.element.textureAsset;                
    
    // mouse events
    this.entity.element.on('mousedown', this.onPress, this);
    this.entity.element.on('mouseup', this.onRelease, this);  
};

// When we press the element assign the active texture
Button.prototype.onPress = function (event) { 
    event.element.textureAsset = this.activeAsset;
};

// When we release the element assign the original texture if 
// we are not hovering or the hover texture if we are still hovering
Button.prototype.onRelease = function (event) {   
    event.element.textureAsset = this.originalTexture;
};


// swap method called for script hot-reloading
// inherit your script state here
// Button.prototype.swap = function(old) { };

// to learn more about script anatomy, please read:
// http://developer.playcanvas.com/en/user-manual/scripting/