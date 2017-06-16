import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { LibModule } from '../lib/lib.module';

import { HomeRoutes } from './home.route';
import { DashboardComponent } from './dashboard/dashboard.component';


@NgModule({
    imports: [
        CommonModule,
        LibModule,
        RouterModule.forChild(HomeRoutes)
    ],
    declarations: [
        DashboardComponent
    ],
    providers: []
})
export class HomeModule { }
