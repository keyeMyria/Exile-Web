import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { UsuariosRoutes } from './usuarios.route';

@NgModule({
    imports: [
        RouterModule.forChild(UsuariosRoutes),
        CommonModule
    ],
    declarations: [],
    providers: []
})
export class UsuariosModule { }
