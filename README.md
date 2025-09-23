# Railway Transport System

A comprehensive railway management system built in Python that handles train operations, ticket purchasing, and user management with three distinct user roles: Admin, Employee, and Regular Users.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No external dependencies required (all modules are built-in)

### Installation & Running
1. Clone or download the project files
2. Navigate to the project directory
3. Run the main application:
```bash
python start_menu.py
```

## 📋 System Overview

The Railway Transport System consists of three main user interfaces:

### 🔐 User Roles & Access

| Role | Username | Password | Access Level |
|------|----------|----------|--------------|
| **Admin** | `admin` | `Today@1404` | Full system management |
| **Employee** | Created by Admin | Created by Admin | Train & Line management |
| **Regular User** | Self-registered | Self-registered | Ticket purchasing |

## 🎯 Main User Flows

### 1. Admin Flow
**Purpose**: System administration and employee management

**Login**: `admin` / `Today@1404`

**Available Operations**:
- ✅ Add new train employees
- ✅ Remove train employees  
- ✅ View employee list with full details
- ✅ Manage employee credentials

**Important Notes**:
- Only admins can create employee accounts
- Employee credentials are displayed in full (including passwords) for admin reference
- Employees must be created before they can access the system

### 2. Employee Flow
**Purpose**: Train and railway line management

**Access**: Login with employee credentials created by admin

**Available Operations**:
- ✅ **Line Management**:
  - Add new railway lines (origin, destination, stations)
  - Update existing lines
  - Remove lines (also removes associated trains)
  - View all lines with detailed information

- ✅ **Train Management**:
  - Add new trains (name, line, speed, quality, price, capacity)
  - Update train properties
  - Remove trains
  - View all trains with specifications

**Important Notes**:
- Trains can only be created after lines are established
- Train quality options: `3stars`, `2stars`, `1star`
- Stop durations are required for each station on the line
- When a line is removed, all associated trains are automatically removed

### 3. Regular User Flow (Primary Focus)
**Purpose**: Ticket purchasing and account management

#### Registration & Login
- **Registration**: Create account with username, email, name, and password
- **Login**: Access with registered credentials
- **Password Requirements**: Must contain letters, numbers, and either @ or &

#### Main User Features

**1. Ticket Purchasing**
- Browse available trains with real-time capacity information
- Select train from available options
- Choose number of tickets (multiple tickets supported)
- Automatic capacity validation
- Payment processing through wallet or saved cards

**2. Wallet Management**
- Add funds to wallet using credit/debit cards
- Real-time balance tracking
- Transaction history recording
- Automatic balance deduction for purchases

**3. Card Management**
- Save multiple payment cards for convenience
- Add new cards with full validation
- Remove saved cards
- View card transaction history
- Use saved cards for wallet top-ups and purchases

**4. Account Management**
- Edit personal information (name, email)
- View transaction history
- Manage payment methods

## 🚂 Train System Behavior

### Sample Trains (Fallback System)
**Important**: If no trains are added to the system by employees, the system will automatically display sample trains:

1. **Raja Train**
   - Route: Rasht → Tehran
   - Capacity: 16 seats
   - Price: 120 Toman

2. **Fadak Train**
   - Route: Babol → Shiraz  
   - Capacity: 10 seats
   - Price: 320 Toman

**⚠️ Potential Conflicts**: These sample trains may cause capacity conflicts or other issues since they're not properly integrated with the line management system. It's recommended that employees add proper trains to avoid conflicts.

### Real Train Integration
- Trains created by employees are properly linked to railway lines
- Real-time capacity tracking (shows available seats)
- Automatic seat reservation and release
- Proper origin/destination mapping from line data

## 💳 Payment System

### Bank Integration
- **API**: Simulated bank API (`BANK.py`)
- **Validation**: Card number (16 digits), expiry (1403-1408), CVV2 (3 digits), password (6 digits)
- **Security**: All payment details are validated before processing
- **Transaction IDs**: Unique payment IDs generated for each transaction

### Payment Methods
1. **Wallet Balance**: Direct deduction from user's wallet
2. **Saved Cards**: Use previously saved payment cards
3. **New Cards**: Enter new card details for one-time use
4. **Hybrid**: Combine wallet balance with card payments

## 📁 File Structure

```
railwayTransportSystem/
├── start_menu.py          # Main entry point
├── main.py               # Regular user flow
├── admin.py              # Admin management
├── final_employee_panel.py # Employee operations
├── user.py               # User management & cards
├── train.py              # Train display & selection
├── final_train.py        # Train management (employee)
├── final_line.py         # Line management (employee)
├── ticket.py             # Ticket issuing system
├── wallet.py             # Wallet & payment management
├── BANK.py               # Payment API simulation
├── utils.py              # Validation utilities
└── requirements.txt      # Dependencies (empty - no external deps)
```

## 🔧 Key Features

### User Experience
- ✅ Intuitive menu-driven interface
- ✅ Comprehensive input validation
- ✅ Real-time capacity checking
- ✅ Transaction history tracking
- ✅ Multiple payment options
- ✅ Error handling with retry options

### System Features
- ✅ Role-based access control
- ✅ Real-time train capacity management
- ✅ Automatic ticket generation
- ✅ File-based data persistence
- ✅ Card management with transaction history
- ✅ Wallet balance management

### Security Features
- ✅ Password complexity requirements
- ✅ Email format validation
- ✅ Card number validation
- ✅ Input sanitization
- ✅ Secure payment processing

## 📝 Usage Examples

### For Regular Users
1. **Start**: Run `python start_menu.py`
2. **Select**: Choose "3. User"
3. **Register**: Create new account or login with existing
4. **Add Funds**: Go to "Manage Cards" → "Add New Card" or use saved card
5. **Buy Tickets**: Select "Buy Ticket" → Choose train → Select quantity → Confirm purchase

### For Employees
1. **Start**: Run `python start_menu.py`
2. **Select**: Choose "2. Employee"
3. **Login**: Use employee credentials created by admin
4. **Add Lines**: Create railway lines with stations
5. **Add Trains**: Create trains on established lines
6. **Manage**: Update or remove trains/lines as needed

### For Admins
1. **Start**: Run `python start_menu.py`
2. **Select**: Choose "1. Admin"
3. **Login**: Use `admin` / `Today@1404`
4. **Manage Employees**: Add, remove, or view employee accounts

## ⚠️ Important Notes

1. **Sample Train Conflicts**: The system shows sample trains when no real trains exist, which may cause capacity conflicts
2. **Data Persistence**: User data, tickets, and transactions are saved to files
3. **Card Validation**: All card details are validated according to Iranian banking standards (1403-1408 for years)
4. **Capacity Management**: Real trains have proper capacity tracking, sample trains may not
5. **Line Dependencies**: Trains can only be created on existing railway lines
6. **Transaction Recording**: All purchases and payments are logged with timestamps

## 🎯 Recommended Workflow

1. **Admin** creates employee accounts first
2. **Employees** add railway lines and then trains
3. **Regular Users** can then purchase tickets from available trains
4. **System** automatically handles capacity, payments, and ticket generation

This ensures a smooth operation without conflicts from sample trains and provides users with a comprehensive railway booking experience.