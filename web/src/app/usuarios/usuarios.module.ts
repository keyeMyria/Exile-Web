import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { UsuariosRoutes } from './route';
import { AsistenteService } from './asistente/asistente.service';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { EditEmpleadoComponent, ListEmpleadoComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';
import { SampleModule } from '../shared';
import { CargoService } from '../configuracion/cargo/cargo.service';
import { PerfilComponent, EditPerfilComponent } from './perfil/perfil.component';
import { PerfilService } from './perfil/perfil.service';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule,
        RouterModule.forChild(UsuariosRoutes)
    ],
    declarations: [
        AsistenteListComponent,
        AsistenteEditComponent,
        EditEmpleadoComponent,
        ListEmpleadoComponent,
        PerfilComponent,
        EditPerfilComponent
    ],
    providers: [
        AsistenteService,
        EmpleadoService,
        CargoService,
        PerfilService
    ]
})
export class UsuariosModule { }
