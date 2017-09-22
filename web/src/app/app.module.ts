import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { NgModule, LOCALE_ID } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SampleModule } from 'componentex';
import { AgmCoreModule } from '@agm/core';



import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';

//
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
    providers: [
        { provide: LOCALE_ID, useValue: 'es-CO' },
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
