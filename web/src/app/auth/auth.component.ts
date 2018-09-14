import { Component, OnInit } from '@angular/core';
import { Router, Event, NavigationEnd, NavigationStart } from '@angular/router';

declare var $: any;

@Component({
    templateUrl: './auth.component.html'
})
export class AuthComponent implements OnInit {

    public test: Date = new Date();

    constructor(private _router: Router) {
        this._router.events.subscribe(this.ckeckRouterEvents);
    }

    ckeckRouterEvents(evn: Event) {
        if (evn instanceof NavigationEnd) {
            setTimeout(function() {
                $('.navbar-collapse').removeClass('in');
                $('.card').removeClass('card-hidden');
            }, 200);
        }
    }

    checkFullPageBackgroundImage() {
        const $page = $('.full-page');
        const image_src = $page.data('image');

        if (image_src !== undefined) {
            const image_container = '<div class="full-page-background" style="background-image: url(' + image_src + ') "/>';
            $page.append(image_container);
        }
    };

    ngOnInit() {
        this.checkFullPageBackgroundImage();
    }

}
