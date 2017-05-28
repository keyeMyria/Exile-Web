import { Routes } from '@angular/router';

export const OperacionRoutes: Routes = [
    {
        path: '', children: [
            { path: '', redirectTo: 'login', pathMatch: 'full' }
        ]
    }
];
