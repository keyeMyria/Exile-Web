import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { SampleModule } from 'componentex';

import { HomeRoutes } from './home.route';
import { DashboardComponent } from './dashboard/dashboard.component';


@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        RouterModule.forChild(HomeRoutes)
    ],
    declarations: [
        DashboardComponent
    ],
    providers: []
})
export class HomeModule { }
