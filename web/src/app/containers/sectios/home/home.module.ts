import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { HomeRoutes } from './home.route';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CardComponent } from '../../../conponent-lib/card/card.component'
@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(HomeRoutes)
    ],
    declarations: [
        CardComponent,
        DashboardComponent
    ],
    providers: []
})
export class HomeModule { }
