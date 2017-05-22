import { Component, OnInit } from '@angular/core';
import { ROUTES } from './sidebar-routes.config';

declare var $:any;

var mda:any = {
   misc: {
       movingTab: '<div class="sidebar-moving-tab"/>',
       isChild: false,
       sidebarMenuActive: ''
   }
};

var sidebarTimer;

@Component({
    moduleId: module.id,
    selector: 'sidebar-cmp',
    templateUrl: 'sidebar.component.html',
})

export class SidebarComponent implements OnInit {
    public menuItems: any[];
    isNotMobileMenu(){
        if($(window).width() > 991){
            return false;
        }
        return true;
    }
    ngOnInit() {
        // $.getScript('../../assets/js/sidebar-moving-tab.js');

        var isWindows = navigator.platform.indexOf('Win') > -1 ? true : false;
        if (isWindows){
           // if we are on windows OS we activate the perfectScrollbar function
            var $sidebar = $('.sidebar-wrapper');
            $sidebar.perfectScrollbar();

        }
        this.menuItems = ROUTES.filter(menuItem => menuItem);

    }


}
