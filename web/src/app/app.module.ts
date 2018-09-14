import { BrowserModule } from '@angular/platform-browser';
import { CommonModule, registerLocaleData } from '@angular/common';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SampleModule } from './shared';
import { AgmCoreModule } from '@agm/core';
import localeCo from '@angular/common/locales/es-CO';


import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';

//
registerLocaleData(localeCo);
@NgModule({
    declarations: [
        AppComponent,
    ],
    imports: [
        CommonModule,
        HttpModule,
        BrowserModule,
        BrowserAnimationsModule,
        FormsModule,
        ReactiveFormsModule,
        AgmCoreModule.forRoot({ apiKey: 'AIzaSyCOmN9BsyRSR0PCmX_r5H-JmvWdUQ3TlDw', libraries: ['places'] }),
        SampleModule.forRoot(),
        AppRouteModule,
        AuthModule
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
