import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SampleModule } from 'componentex';
import { OperacionRoutes } from './route';

import { TipoclienteListComponent, TipoclienteEditComponent } from './tipocliente/tipocliente.component';
import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';

import { TipoclienteService } from './tipocliente/tipocliente.service';
import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(OperacionRoutes)
    ],
    declarations: [
        TipoclienteListComponent,
        TipoclienteEditComponent,
        ClienteEditComponent,
        ClienteListComponent,
        LugarEditComponent,
        LugarListComponent,
    ],
    providers: [
        TipoclienteService,
        ClienteService,
        LugarService
    ]
})
export class OperacionModule { }
