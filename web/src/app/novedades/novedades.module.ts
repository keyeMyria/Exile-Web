import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DateValueAccessorModule } from 'angular-date-value-accessor';
import { ReportesComponent } from './reportes/reportes.component';
import { SampleModule } from 'componentex';

@NgModule({
    imports: [
        CommonModule,
        SampleModule,
        FormsModule,
        ReactiveFormsModule,
        DateValueAccessorModule
    ],
    declarations: [ReportesComponent],
    providers: [

    ]
})
export class NovedadesModule { }
