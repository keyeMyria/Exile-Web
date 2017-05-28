import { Routes } from '@angular/router';

export const HomeRoutes: Routes = [
    {
        path: '', children: [
            { path: '', redirectTo: 'login', pathMatch: 'full' }
        ]
    }
];
