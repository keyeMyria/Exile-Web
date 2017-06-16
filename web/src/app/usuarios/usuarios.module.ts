import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LibModule } from '../lib/lib.module';
import { UsuariosRoutes } from './usuarios.route';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { EmpleadoComponent } from './empleado/empleado.component';
import { AsistenteService } from '../services/usuarios/asistente.service';

@NgModule({
    imports: [
        CommonModule,
        LibModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(UsuariosRoutes)
    ],
    declarations: [
        AsistenteComponent, AsistenteListComponent, AsistenteEditComponent,
        EmpleadoComponent
    ],
    providers: [ AsistenteService ]
})
export class UsuariosModule { }
