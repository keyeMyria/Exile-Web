import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { UsuariosRoutes } from './route';
import { AsistenteService } from './asistente/asistente.service';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AdminService } from './admin/admin.service';
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
        AdminComponent,
        EditAdminComponent,
        ListAdminComponent,
        CargoListComponent,
        EditCargoComponent
    ],
    providers: [
        AsistenteService,
        AdminService,
        CargoService
    ]
})
export class UsuariosModule { }
