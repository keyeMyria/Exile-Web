import { Component, ElementRef, NgZone, OnInit, ViewChild, Output, Input, EventEmitter } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MapsAPILoader, GoogleMapsAPIWrapper } from '@agm/core';
// import { } from 'googlemaps';

declare var navigator: any;

@Component({
    selector: 'ex-gmap',
    templateUrl: './exgmap.component.html',
    styleUrls: ['./exgmap.component.scss']
})
export class ExgmapComponent implements OnInit {

    @ViewChild('search')
    public searchElementRef: ElementRef;
    @Input()
    public latitude = 4.570868;
    @Input()
    public longitude = -74.297333;
    public searchControl: FormControl = new FormControl();
    @Input()
    public zoom = 5;
    public markerdraggable = true;
    @Output()
    public coordsChange = new EventEmitter();
    public currentPosition = true;

    constructor(private mapsAPILoader: MapsAPILoader, private ngZone: NgZone, private wrapper: GoogleMapsAPIWrapper) { }

    ngOnInit() {
        // set current position
        this.setCurrentPosition();

        // load Places Autocomplete
        // this.mapsAPILoader.load().then(() => {
        //     const autocomplete = new google.maps.places.Autocomplete(this.searchElementRef.nativeElement);
        //     autocomplete.addListener('place_changed', () => {
        //         this.ngZone.run(() => {
        //             const place: google.maps.places.PlaceResult = autocomplete.getPlace();
        //             if (place.geometry === undefined || place.geometry === null) {
        //                 return;
        //             }
        //             this.coords = { lat: place.geometry.location.lat(), lng: place.geometry.location.lng() }
        //         });
        //     });
        // });
    }

    onDragEnd(event) {
        this.coords = event.coords;
    }

    onKeydown(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            return false;
        }
    }

    private setCurrentPosition() {
        if (this.currentPosition) {
            if ('geolocation' in navigator) {
                navigator.geolocation.getCurrentPosition((position) => {
                    this.coords = { lat: position.coords.latitude, lng: position.coords.longitude }
                    this.zoom = 18;
                });
            }
        }
    }

    public get coords(): Coord {
        return { lat: this.latitude, lng: this.longitude };
    }

    public set coords(coords: Coord) {
        this.latitude = coords.lat;
        this.longitude = coords.lng;
        this.coordsChange.emit(coords);
    }
}

interface Coord {
    lat: number;
    lng: number;
}
