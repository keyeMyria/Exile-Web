import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { ReportesListComponent } from './reportes/reportes.component';
import { SampleModule } from 'componentex';
import { ReportesService } from './reportes/reportes.service';
import { NovedadesRoutes } from './route';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule,
        RouterModule.forChild(NovedadesRoutes)
    ],
    declarations: [ReportesListComponent],
    providers: [
        ReportesService
    ]
})
export class NovedadesModule { }
