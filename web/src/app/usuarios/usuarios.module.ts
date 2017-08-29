import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { UsuariosRoutes } from './route';
import { AsistenteService } from './asistente/asistente.service';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { EditEmpleadoComponent, ListEmpleadoComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';
import { SampleModule } from 'componentex';
import { CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { CargoService } from './cargo/cargo.service';

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
        CargoListComponent,
        EditCargoComponent
    ],
    providers: [
        AsistenteService,
        EmpleadoService,
        CargoService
    ]
})
export class UsuariosModule { }
