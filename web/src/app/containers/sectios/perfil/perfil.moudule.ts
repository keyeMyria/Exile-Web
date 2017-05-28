import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { PerfilRoutes } from './perfil.route';

@NgModule({
    imports: [
        RouterModule.forChild(PerfilRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class PerfilModule { }
