import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AgmCoreModule } from '@agm/core';
import { SampleModule } from 'componentex';
import { OperacionRoutes } from './route';

import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';

import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';
import { TipoclienteService } from '../configuracion/tipocliente/tipocliente.service';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        AgmCoreModule,
        RouterModule.forChild(OperacionRoutes)
    ],
    declarations: [
        ClienteEditComponent,
        ClienteListComponent,
        LugarEditComponent,
        LugarListComponent,
    ],
    providers: [
        ClienteService,
        LugarService,
        TipoclienteService
    ]
})
export class OperacionModule { }
