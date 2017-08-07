import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRouteModule } from './app.route.module';
import { AppComponent } from './app.component';
import { AuthModule } from './auth/auth.module';
import { AuthService } from './auth/auth.service';
import { CallService } from '../lib/services/call.service';
import { LibModule } from '../lib/lib.module'
@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        HttpModule,
        CommonModule,
        BrowserAnimationsModule,
        LibModule,
        AppRouteModule,
        AuthModule
    ],
    providers: [CallService],
    bootstrap: [AppComponent]
})
export class AppModule { }
