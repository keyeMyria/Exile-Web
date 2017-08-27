import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SampleModule } from 'componentex';

import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';


@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        CommonModule,
        HttpModule,
        BrowserModule,
        BrowserAnimationsModule,
        SampleModule.forRoot(),
        AppRouteModule,
        AuthModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule { }
