import { Component, OnInit } from '@angular/core';
import { AppMenuMeta } from '../../app.routing';
declare var $: any;

@Component({
    selector: 'ex-sidebar',
    templateUrl: './sidebar.component.html'
})
export class SidebarComponent implements OnInit {

    menuInfo: any[];

    constructor() { }

    ngOnInit() {
        const isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;
        if (isWindows) {
            // if we are on windows OS we activate the perfectScrollbar function
            const $sidebar = $('.sidebar-wrapper');
            $sidebar.perfectScrollbar();
        }
        this.menuInfo = AppMenuMeta.filter(menuItem => menuItem);
    }

    isNotMobileMenu() {
        if ($(window).width() > 991) {
            return false;
        }
        return true;
    }

}
