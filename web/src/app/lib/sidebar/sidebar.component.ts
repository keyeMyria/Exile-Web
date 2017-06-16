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
        $.getScript('../../assets/js/sidebar-moving-tab.js');

        this.menuInfo = AppMenuMeta.filter(menuItem => menuItem);
    }

    isNotMobileMenu() {
        if ($(window).width() > 991) {
            return false;
        }
        return true;
    }

}
