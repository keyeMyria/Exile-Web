import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { LibModule } from '../../lib/lib.module';
import { UsuariosRoutes } from './route';
import { AsistenteService } from './asistente/asistente.service';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AdminService } from './admin/admin.service';

@NgModule({
    imports: [
        CommonModule,
        LibModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule,
        RouterModule.forChild(UsuariosRoutes)
    ],
    declarations: [
        AsistenteComponent,
        AsistenteListComponent,
        AsistenteEditComponent,
        AdminComponent,
        EditAdminComponent,
        ListAdminComponent
    ],
    providers: [
        AsistenteService,
        AdminService
    ]
})
export class UsuariosModule { }
