import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { LibModule } from '../lib/lib.module';
import { CovalentDataTableModule } from '@covalent/data-table';

import { UsuariosRoutes } from './usuarios.route';
import { AsistenteComponent } from './asistente/asistente.component';
import { EmpleadoComponent } from './empleado/empleado.component';

@NgModule({
    imports: [
        RouterModule.forChild(UsuariosRoutes),
        CommonModule,
        LibModule,
        CovalentDataTableModule.forRoot()
    ],
    declarations: [AsistenteComponent, EmpleadoComponent],
    providers: []
})
export class UsuariosModule { }
