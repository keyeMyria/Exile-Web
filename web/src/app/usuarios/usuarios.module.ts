import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { UsuariosRoutes } from './route';
import { AsistenteService } from './asistente/asistente.service';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AdminService } from './admin/admin.service';
import { SampleModule } from 'componentex';
import { CargoComponent } from './cargo/cargo.component';
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
        CargoComponent
    ],
    providers: [
        AsistenteService,
        AdminService
    ]
})
export class UsuariosModule { }
