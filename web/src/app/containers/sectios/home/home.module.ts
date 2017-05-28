import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { HomeRoutes } from './home.route';

@NgModule({
    imports: [
        RouterModule.forChild(HomeRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class InformesModule { }
